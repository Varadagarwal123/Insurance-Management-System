from django.contrib import admin
from .models import *
from django.utils import timezone
# Register your models here.
admin.site.register(CustomerDetail)
admin.site.register(Ajents)

from .models import Appointment
from .forms import AppointmentAdminForm

class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentAdminForm
    list_display = ('customer', 'agent', 'appointment_date', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('customer__user__username', 'agent__name')
    
admin.site.register(Appointment, AppointmentAdmin)


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'name', 'coverage_amount', 'premium', 'term')
    search_fields = ('policy_number', 'name')
    list_filter = ('term',)

@admin.register(PolicyApplication)
class PolicyApplicationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'policy', 'application_date', 'is_approved')
    list_filter = ('is_approved',)

    def save_model(self, request, obj, form, change):
        if obj.is_approved and 'is_approved' in form.changed_data:
            obj.approval_date = timezone.now()
        super().save_model(request, obj, form, change)