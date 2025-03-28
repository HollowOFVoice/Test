from django.contrib import admin
from main.models import Book

admin.site.register(Book)  # Только регистрация моделей из main