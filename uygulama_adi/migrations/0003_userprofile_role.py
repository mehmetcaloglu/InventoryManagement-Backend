# Generated by Django 5.0.1 on 2024-01-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama_adi', '0002_remove_userprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(default='staff_manager', max_length=50),
        ),
    ]