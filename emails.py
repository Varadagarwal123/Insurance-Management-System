from django.core.mail import send_mail
from django.conf import settings

def send_appointment_email(appointment):
    subject = 'Appointment Scheduled'
    message = f'Dear {appointment.customer.user.username},\n\n' \
              f'Your appointment has been scheduled with {appointment.agent.name} at the following time slot: {appointment.appointment_date}.\n\n' \
              'Thank you!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [appointment.customer.user.email]
    
    send_mail(subject, message, from_email, recipient_list)
