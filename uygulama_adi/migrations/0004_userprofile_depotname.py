# Generated by Django 5.0.1 on 2024-01-13 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama_adi', '0003_userprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='depotname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uygulama_adi.depot'),
        ),
    ]