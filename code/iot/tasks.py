from __future__ import absolute_import, unicode_literals
from celery import shared_task
from iot.models import *
from user.models import *
from iot.store import DEFAULT_STORE_STATUS

@shared_task(name='create_machine_session', max_tries=1)
def create_machine_session():        
    status = StoreModeChange.objects.order_by('created_at').values_list('status', flat=True).last()
    if not status:
        status = DEFAULT_STORE_STATUS
    store_session = create_store_session(status=status)
    store_session.save()
    
    print(' created store_session', store_session.id, store_session.status)
    return("New machine session created")

def create_store_session(status):
    store_session = StoreSessions.objects.create(status=status)
    store_session.save()
    return store_session

def get_current_store_session():
    store_session = StoreSessions.objects.order_by('created_at').values_list('id', flat=True).last()
    print(store_session)
    return store_session

def get_current_store_session_status():
    store_session_status = StoreSessions.objects.order_by('created_at').values_list('status', flat=True).last()
    print(store_session_status)
    return store_session_status

def create_mode_control(status):
    mode_control = StoreModeChange(status=status)
    is_mode_control_created = mode_control.save()
    return is_mode_control_created

def create_weight_change_event(machine_id, scale_id, weight_change, status, session_id):
    weight_change_event = WeightChanges(machine_id=machine_id, scale_id=scale_id, weight_change=weight_change, status=status, session_id=session_id)
    is_weight_chane_event_created = weight_change_event.save()
    return is_weight_chane_event_created