from django.db import models
import uuid

class RegisterData(models.Model):
    userId = models.UUIDField(primary_key= True, unique = True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    