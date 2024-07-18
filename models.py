from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class CustomerDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='customer_details')
    Phone_number=models.CharField(max_length=15,null=True)
    Address=models.CharField(max_length=100,null=True)
    otp = models.CharField(max_length=25,default='0000')

    def __str__(self):
        return self.user.username

class Ajents(models.Model):
    address = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(unique=True, null=True)
    is_available = models.BooleanField(default=True)
    available_from = models.TimeField(null=True, blank=True)
    available_to = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]

    customer = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE, related_name='appointments')
    agent = models.ForeignKey(Ajents, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.customer.user.username} - {self.appointment_date}"
    
class Policy(models.Model):
    policy_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField(help_text="Term in years")

    def __str__(self):
        return self.name
    
class PolicyApplication(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.username} - {self.policy.name}"
    


