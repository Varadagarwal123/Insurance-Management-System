# Generated by Django 5.0.4 on 2024-05-29 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0015_alter_appointment_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetail',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='customerdetail',
            name='Phone_number',
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_details', to=settings.AUTH_USER_MODEL),
        ),
    ]
