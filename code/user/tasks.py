from user.models import *


def create_user_session(user_id, store_session_id, phone_number, role, status):
    user_session = UserSessions(user_id=user_id, session_id=store_session_id, phone_number=phone_number, role=role, status=status)
    is_user_session_created = user_session.save()
    return is_user_session_created

def create_user_cycle(login_time, logout_time, user_id):
    user_cycle = UserCycle(login_time=login_time, logout_time=logout_time, user_id=user_id)
    is_user_cycle_created = user_cycle.save()
    return is_user_cycle_created
