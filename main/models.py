from django.db import models
from users.models import CustomUser
from django.urls import reverse

class Book(models.Model):
    GENRE_CHOICES = [
        ('fantasy', 'Фэнтези'),
        ('classic', 'Классика'),
        ('detective', 'Детектив')
    ]

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    condition = models.CharField(max_length=100)



