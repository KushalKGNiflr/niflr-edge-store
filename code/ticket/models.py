from django.db import models
import uuid

class Tickets(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4) 
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    weight_change_events = models.TextField()
    store_session = models.TextField()
    user_id = models.UUIDField(null=False)
    user_session_id = models.UUIDField(null=False)
    video = models.TextField()
    machine_id = models.CharField(null=True, max_length=100)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ticket"