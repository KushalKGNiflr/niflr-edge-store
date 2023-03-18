from django.shortcuts import render
from iot.models import *
from iot.serializers import *
from iot.store import *
from iot.tasks import *
from user.tasks import *
from rest_framework import viewsets, permissions
import logging
from rest_framework.views import APIView
from django.http.response import HttpResponse
import logging
import json
import pandas as pd 

class WeightViewSet(viewsets.ModelViewSet):
    queryset = WeightChanges.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticated]

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticated]

class StoreSessionViewSet(viewsets.ModelViewSet):
    queryset = StoreSessions.objects.all()
    serializer_class = StoreSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

class StoreModeViewSet(viewsets.ModelViewSet):
    queryset = StoreModeChange.objects.all()
    serializer_class = StoreModeSerializer
    permission_classes = [permissions.IsAuthenticated]

class HeartbeatView(APIView):
    global DF
    DF = None
    logger = logging.getLogger('heartbeat')
    all_hb = logging.getLogger('all_hb')

    def post(self, request, *args, **kwargs):
        global DF
        payload = json.loads(request.body)
        print(payload)
        self.all_hb.debug(payload)
        
        payload_str = payload['payload']
        payload_dict = json.loads(payload_str)
        scales_data = payload_dict['scales']
        machineId_data = payload_dict['machineId']
        scales_df = pd.DataFrame(scales_data, columns=['scaleId', 'minWeight', 'maxWeight', 'currentWeight'])
        scales_df = scales_df.drop(columns=['minWeight','maxWeight'])
        scales_df[['currentWeight']] = scales_df[['currentWeight']].apply(pd.to_numeric)
        # print(DF)
        if DF is not None:
            if scales_df.equals(DF):
                print("Data is same as previous request")
                self.logger.debug("Data is same as previous request")
            else:
                print("Data is different from previous request")
                self.logger.debug("Data is different from previous request")
                DF_Final = pd.merge(DF, scales_df, on='scaleId', how='inner')                
                DF_Final['weight_change']=(DF_Final['currentWeight_x']-DF_Final['currentWeight_y'])
                # print(DF_Final)
                print(DF_Final[DF_Final['weight_change'] != 0])
                self.logger.debug("\n%s",DF_Final[DF_Final['weight_change'] != 0])

                nor = DF_Final.shape[0]

                session_id = StoreSessions.objects.order_by('created_at').values_list('id', flat=True).last()
                print(session_id)

                for i in range(nor):
                    if DF_Final.weight_change[i]>=0.01:
                        print("Item picked, weight change detected")
                        self.logger.debug("Item picked, weight change detected")
                        create_weight_change_event(str(machineId_data), str(DF_Final.scaleId[i]), DF_Final.weight_change[i], PICK, str(session_id))
                        
                    elif DF_Final.weight_change[i]<=-0.01:
                        print("Item placed, weight change detected")
                        self.logger.debug("Item placed, weight change detected")
                        create_weight_change_event(str(machineId_data), str(DF_Final.scaleId[i]), (DF_Final.weight_change[i])*(-1), PLACE, str(session_id))                        

        else:
            print("First iteration")
            self.logger.debug("First iteration")

        DF = scales_df.copy()
        return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
    

class ModeControlView(APIView):
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        status = payload['status']
        update_store_status(status)
        create_mode_control(str(status))
        create_store_session(str(status))
        return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
    
class lock(APIView):
    def post(self, request):
        return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')