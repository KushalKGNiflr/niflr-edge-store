from django.shortcuts import render
from .models import *
from .serializers import *
from iot.models import *
from camera.models import *
from iot.store import *
from .tasks import *
from rest_framework import viewsets, permissions
from django.conf import settings

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

def generate_ticket(start_time, end_time, user_id, user_session_id):        
    machs = Machines.objects.values_list('machine_id', flat=True)

    print('\nMatching Machines ------------>')
    print(machs)

    for mach in machs:
        mac = int(mach)
        print("Machine specific:")
        print(mac)

        print('\nMatching Store Session IDs: ------------>')
        session_ids = StoreSessions.objects.filter(created_at__gte=start_time, created_at__lte=end_time).values_list('id', flat=True)
        store_session = [str(uuid) for uuid in session_ids]
        print(store_session)

        print('\n\nAll Weight Change Events: ---------------->\n')
        weight_change_ids = WeightChanges.objects.filter(machine_id=mac, created_at__gte=start_time, created_at__lte=end_time).values_list('id', flat=True)        
        event_session = [str(uuid) for uuid in weight_change_ids]
        print(event_session)

        print('\n\nAll Videos: ---------------->\n')
        videos = Videos.objects.filter(machine_id=mac, created_at__gte=start_time, created_at__lte=end_time).values_list('id', flat=True)        
        video_session = [str(uuid) for uuid in videos]
        print(video_session)

        create_tickets(str(start_time), str(end_time), str(store_session), str(event_session), user_id, str(video_session), str(mac), REVIEW_PENDING, str(user_session_id))