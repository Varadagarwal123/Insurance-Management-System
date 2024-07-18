from django import forms
from .models import *
from . import models

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'})
    )

    class Meta:
        model = Appointment
        fields = ['customer', 'agent', 'appointment_date']

class AppointmentAdminForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']

class PolicyApplicationForm(forms.ModelForm):
    policy = forms.ModelChoiceField(queryset=Policy.objects.all(), label="Select Policy")

    class Meta:
        model = PolicyApplication
        fields = ['policy']
