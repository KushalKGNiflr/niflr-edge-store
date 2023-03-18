from django.db import models
import uuid

class WeightChanges(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    scale_id = models.CharField(null=False, max_length=10)
    machine_id = models.CharField(null=False, max_length=20)
    weight_change = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.UUIDField(null=False)    
    status = models.CharField(null=False, max_length=255)

class Machines(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    machine_id = models.CharField(null=False, max_length=100)
    display_name = models.CharField(null=False, max_length=100)
    store_id = models.UUIDField(null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "Machine"

class StoreSessions(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(null=False, max_length=255)

class StoreModeChange(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    store_id = models.UUIDField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(null=False, max_length=255)