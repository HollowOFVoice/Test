from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    address = models.TextField()