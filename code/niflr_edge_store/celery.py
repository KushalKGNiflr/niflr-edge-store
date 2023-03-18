from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niflr_edge_store.settings')

app = Celery('niflr_edge_store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False
app.conf.timezone = "Asia/Calcutta"

app.conf.beat_schedule = {
    'machine-session-generate-after-30-sec': {
        'task': 'create_machine_session',
        'schedule': 30.0,
        'options': {
            'expires': 3.0,
        },
    }
}

app.autodiscover_tasks()
# tasks = app.tasks.keys()
# print("List of tasks: ", tasks)