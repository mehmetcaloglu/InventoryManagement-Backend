# Generated by Django 5.0.1 on 2024-01-10 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama_adi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]