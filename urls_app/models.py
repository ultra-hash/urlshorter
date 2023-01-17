from django.db import models
import uuid
# Create your models here.
class Shorturls(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    target_url = models.URLField(null=False)
    short_url = models.URLField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.ForeignKey('Users', null=True, on_delete=models.CASCADE)

class Users(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    username = models.CharField(max_length=40, unique=True, null=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True, null=False)
    phone = models.CharField(unique=True, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    