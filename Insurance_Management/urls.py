"""
URL configuration for Insurance_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Insurance import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('registration/', views.registration, name='registration'),
    path('Customer_login/', views.Customer_login, name='Customer_login'),
    path('Customer_home/', views.Customer_home, name='Customer_home'),
    path('agents/', views.agent_list, name='agent_list'),
    path('Contact_Us/', views.Contact_Us, name='Contact_Us'),
    path('agents/', views.agent_list, name='agent_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('manage/', views.manage_appointments, name='manage_appointments'),
    path('update/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('status/', views.view_appointment_status, name='view_appointment_status'),
    path('about/', views.about_page, name='about'),
    path('logout/', views.logout_success_view, name='logout'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accepted-policies/', views.accepted_policy_details, name='accepted_policy_details'),
    path('apply/', views.apply_policy, name='apply_policy'),
    path('Customer_login/forgot_password/', views.forgot_password, name='forgot_password'),
   
]
