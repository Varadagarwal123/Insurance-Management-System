from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LogoutView
from .models import *
from django.contrib.auth import login,logout,authenticate
import folium
import geocoder
import time
from .forms import *
from django.contrib.auth.decorators import login_required,user_passes_test
import random
from django.core.cache import cache
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings


# Create your views here.
def home_page(request):
    return render(request,'home_page.html')

def Customer_home(request):
    return render(request,'Customer_home.html')
def Contact_Us(request):
    return render(request,'Contact_Us.html')

def Customer_login(request):
    error=""
    if request.method=='POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'Customer_login.html',locals())
def about_page(request):
    return render(request, 'about.html')

def registration(request):
    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        pn = request.POST.get('Phone_number')
        lc = request.POST.get('Address')
        em = request.POST.get('email')
        pwd = request.POST.get('pwd')
        
        if not (fn and ln and pn and lc and em and pwd):
            messages.error(request, 'All fields are required.')
            return render(request, 'registration.html')
        
        try:
            user = User.objects.create_user(
                first_name=fn,
                last_name=ln,
                username=em,
                password=pwd,
                email=em, # Ensure the email field is set in the User model
            )
            CustomerDetail.objects.create(user=user, Phone_number=pn, Address=lc)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page or another page
        except User.DoesNotExist:
            messages.error(request, 'An error occurred during registration. Please try again.')
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {e}')
    return render(request, 'registration.html')

def agent_list(request):
    agents = Ajents.objects.all()

    # Create a map centered at a certain location
    map = folium.Map(location=[26, 80], zoom_start=6)

    # Add markers for each agent's address
    for agent in agents:
        try:
            # Use geocoder to get the location coordinates based on the address
            location = geocoder.osm(agent.address)
            if location.ok:
                lat = location.latlng[0]
                lon = location.latlng[1]

                # Add marker to the map
                folium.Marker(location=[lat, lon], tooltip="Click for more",
                               popup=(agent.name,agent.email)).add_to(map)

            # Introduce a delay to ensure compliance with the rate limit
            time.sleep(2)  # Sleep for 1 second after each request
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error processing agent '{agent.name}': {str(e)}")

    # Render map to HTML
    map_html = map._repr_html_()

    return render(request, 'agent_list.html', {'agents': agents, 'map_html': map_html})
def logout_success_view(request):
    return render(request, 'logout.html')
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

@staff_member_required
def manage_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'manage_appointments.html', {'appointments': appointments})

@staff_member_required
def update_appointment_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentAdminForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('manage_appointments')
    else:
        form = AppointmentAdminForm(instance=appointment)
    return render(request, 'update_appointment_status.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')


def view_appointment_status(request):
    try:
        customer = CustomerDetail.objects.get(user=request.user)
        appointments = Appointment.objects.filter(customer=customer)
        
        # Debug print statements
        for appointment in appointments:
            print(f"Appointment: {appointment.appointment_date}, Status: {appointment.status}")
            
    except CustomerDetail.DoesNotExist:
        appointments = []

    return render(request, 'view_appointment_status.html', {'appointments': appointments})

from .models import PolicyApplication

@login_required
def accepted_policy_details(request):
    customer = request.user
    accepted_policies = PolicyApplication.objects.filter(customer=customer, is_approved=True)

    return render(request, 'accepted_policy_details.html', {'accepted_policies': accepted_policies})

def apply_policy(request):
    if request.method == 'POST':
        form = PolicyApplicationForm(request.POST)
        if form.is_valid():
            policy = form.cleaned_data['policy']
            customer = request.user  # Directly use the user as the customer

            # Process the application and save it
            PolicyApplication.objects.create(
                customer=customer,
                policy=policy,
            )
            return redirect('accepted_policy_details')  # Redirect to a success page or policy list
    else:
        form = PolicyApplicationForm()

    return render(request, 'apply_policy.html', {'form': form})

def forgot_password(request):
    return render(request,'forgot_password.html')

