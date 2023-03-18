from django.shortcuts import render
from .models import *
from .tasks import *
from .serializers import *
from iot.models import *
from iot.serializers import *
from iot.store import *
from ticket.views import *
from iot.tasks import *
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
import jwt
from django.http.response import HttpResponse
import json
from django.conf import settings
from django.utils import timezone


class UserSessionViewSet(viewsets.ModelViewSet):
    queryset = UserSessions.objects.all()
    serializer_class = UserSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCycleViewSet(viewsets.ModelViewSet):
    queryset = UserCycle.objects.all()
    serializer_class = UserCycleSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

class EntryControlView(APIView):
    def post(self, request, *args, **kwargs):
        print('Entry process start')
        val = input('\nEnter Value: ')
        encrypted_token = bytes(val, 'utf-8')
        print(type(encrypted_token))  

        # JWT token secret        
        secret_key = 'mysecretkey'
        try:
            payload_rec = jwt.decode(encrypted_token, secret_key, algorithms=['HS256'])
            print(payload_rec)
        except jwt.exceptions.InvalidSignatureError:
            print('Invalid User')
        
        user_role = payload_rec['role']

        if get_current_store_session_status() == "REFILLMENT_MODE" and user_role == "customer":
            print("Access Denied!!! System under Refillment Mode")
            return HttpResponse(json.dumps({'status': 'Access Denied!!! System under Refillment Mode'}), content_type='application/json')
                    
        elif get_current_store_session_status() == "MAINTENANCE_MODE" and (user_role == "customer" or user_role == "operations"):
            print("Access Denied!!! System under Maintenance Mode")
            return HttpResponse(json.dumps({'status': 'Access Denied!!! System under Maintenance Mode'}), content_type='application/json')

        else:              
            # Fetch last store session ID and create new user entry session
            store_session_id = get_current_store_session()
            create_user_session(payload_rec['id'], store_session_id, payload_rec['phoneNumber'], payload_rec['role'], ENTRY)
            print("User Session Created")
            return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')        

class ExitControlView(APIView):
    def post(self, request, *args, **kwargs):
        print('Exit process start')
        val = input('\nEnter Value: ')
        encrypted_token = bytes(val, 'utf-8')
        print(type(encrypted_token))  

        # JWT token secret        
        secret_key = 'mysecretkey'
        try:
            payload_rec = jwt.decode(encrypted_token, secret_key, algorithms=['HS256'])
            print(payload_rec)
        except jwt.exceptions.InvalidSignatureError:
            print('Invalid User')
        
        # Fetch last store session ID and create new user exit session

        store_session_id = get_current_store_session()
        create_user_session(payload_rec['id'], store_session_id, payload_rec['phoneNumber'], payload_rec['role'], EXIT)

        current_time = timezone.now()
        end_time_gen = timezone.localtime(current_time)
        end_time_gen = str(end_time_gen)
        end_time = end_time_gen[:-3] + end_time_gen[-2:].replace(':', '')               

        latest_session = UserSessions.objects.filter(user_id=payload_rec['id']).filter(status=ENTRY).order_by('-created_at').values_list('created_at', flat=True).first()

        print('\nRequired Login Time : ------------>')
        start_time = latest_session
        start_time = start_time.strftime('%Y-%m-%d %H:%M:%S.%f%z')

        print("Start Time:", start_time)
        print("End Time:", end_time)

        # Input into User Cycle Table #

        create_user_cycle(str(start_time), str(end_time), payload_rec['id'])
        user_session_id = UserCycle.objects.filter(user_id=payload_rec['id']).order_by('-created_at').values_list('id', flat=True).first()
        
        print('\n User Session ID : ------------>')                
        print(user_session_id)

        # Ticket API Call

        generate_ticket(str(start_time), str(end_time), payload_rec['id'], str(user_session_id))
    
        return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')        