# Generated by Django 5.0.1 on 2024-01-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama_adi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
