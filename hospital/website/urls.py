"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, re_path
from django.shortcuts import render
from . import views

	

urlpatterns = [
	path('home/', views.home, name = 'home'),
	path('skincare/', views.skincare, name='skincare'),
	path('eyecare/', views.eyecare, name='eyecare'),
	path('entcare/', views.entcare, name='entcare'),
	path('makeappointment/', views.makeAppointment, name='makeappointment'),
	path('calendar/', views.calendar, name='calendar'),
	path('patientaccount/', views.patientAccount, name='patientaccount'),
	# re_path(r'^api/clinicdetails/(?P<pk>\d+)$', views.load_clinicdetails, name='clinic_clinicdetails'),
	path('api/designation_employees/', views.load_designation_employees, name='designation_employees'),
	re_path(r'^api/doctor_clinic_date/', views.load_doctor_clinic_date, name='doctor_clinic_date'),
	re_path(r'^api/clinic_date_details/(?P<pk>\d+)$', views.load_clinic_date_details, name='clinic_date_details'),
	#path('newsdetails/', views.newsdetails, name = 'newsdetails'),
 	path('newsdetails/<str:pk>', views.newsread, name = 'newsread'),
 	re_path(r'^newsdetails/(?P<pk>\d+)?$', views.newsdetails, name = 'newsdetails'),

 	path('newsdetails2/<str:pk>', views.newsread2, name = 'newsread2'),
 	re_path(r'^newsdetails2/(?P<pk>\d+)?$', views.newsdetails2, name = 'newsdetails2'),
 	path('confirm/', views.confirm, name='confirm'),

 	path('newsview/', views.newsview, name='newsview'),
 	#re_path(r'^newsview/(?P<pk>\d+)?$', views.newsview, name = 'newsview'),

]



	# path('appoinmentstatus/', views.appoinmentstatus, name = 'appoinmentstatus'),
	# path('update_appoinmentstatus/<str:pk>', views.updateappoinmentstatus, name = 'update_appoinmentstatus'),
	# path('deleteappoinmentstatus/<str:pk>', views.deleteappoinmentstatus, name = 'deleteappoinmentstatus'),