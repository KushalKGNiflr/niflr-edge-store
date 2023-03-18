from django.db import models
import uuid

class UserSessions(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    user_id = models.UUIDField(null=False)
    session_id = models.UUIDField(null=False)
    status = models.CharField(null=False, max_length=255)
    phone_number = models.CharField(null=False, max_length=10)
    role = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserCycle(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    user_id = models.UUIDField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField(null=False)
    logout_time = models.DateTimeField(null=False)

class UserDetails(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(null=False, max_length=10)
    role = models.CharField(null=False, max_length=255)

class Carts(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    user_session_id = models.UUIDField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    item_id = models.UUIDField(null=False)
    item_name = models.CharField(null=False, max_length=255)
    price = models.IntegerField(null=False)
    role = models.CharField(null=False, max_length=255)