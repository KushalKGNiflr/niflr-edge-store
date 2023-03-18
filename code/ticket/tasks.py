from .models import *


def create_tickets(start_time, end_time, store_session, weight_change_events, user_id, video, machine_id, status, user_session_id):
    ticket = Tickets(start_time=start_time, end_time=end_time, store_session=store_session, weight_change_events=weight_change_events, user_id=user_id, video=video, machine_id=machine_id, status=status, user_session_id=user_session_id)
    is_ticket_created = ticket.save()
    return is_ticket_created
