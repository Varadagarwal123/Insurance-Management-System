from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomerDetail
from .models import Appointment
from .emails import send_appointment_email

@receiver(post_save, sender=Appointment)
def appointment_approved(sender, instance, **kwargs):
    if instance.status == 'A' and kwargs.get('created', False) == False:  # Ensure it's an update and status is 'Accepted'
        send_appointment_email(instance)