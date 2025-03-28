# Generated by Django 5.1.7 on 2025-03-28 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('fantasy', 'Фэнтези'), ('classic', 'Классика'), ('detective', 'Детектив')], max_length=50)),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
    ]
