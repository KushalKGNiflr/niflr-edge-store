from django.db import models
import uuid
import random
import string
from django.db import models

def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


class Videos(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    start_time = models.DateTimeField(null=False, max_length=50)
    end_time = models.DateTimeField(null=False, max_length=50)
    session_id = models.UUIDField(null=True) #null=True for testing
    video_path_local = models.TextField()
    video_path_cloud = models.TextField()
    machine_id = models.CharField(null=False, max_length=20)
    store_id = models.UUIDField(null=False)
    tag = models.CharField(null=True, max_length=100)   #Entry, Exit, In-store, Out-of-store
    extra_data = models.TextField(null=True)

    class Meta:
        verbose_name = "Video"

class Cameras(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(null=True, max_length=100, default=generate_random_id) #Unique 4 digit charID
    tag = models.CharField(null=True, max_length=100)   #Entry, Exit, In-store, Out-of-store
    model_number = models.CharField(null=True, max_length=100)
    company = models.CharField(null=True, max_length=100)
    store_id = models.UUIDField(null=True)
    operation_status = models.CharField(null=True, max_length=100) #ON, OFF
    machine_id = models.CharField(null=True, max_length=100)    
    rtsp_path = models.CharField(null=True, max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "Camera"

class Scanners(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    model_number = models.CharField(null=True, max_length=100)
    company = models.CharField(null=True, max_length=100)
    store_id = models.CharField(null=True, max_length=100)
    operation_status = models.CharField(null=True, max_length=100) #ON, OFF
    tag = models.CharField(null=True, max_length=100)   #Entry, Exit
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "Scanner"