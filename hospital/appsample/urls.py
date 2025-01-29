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
	path('customer/', views.customer),
	path('products/', views.products),
	path('reportDiagnosis/', views.reportDiagnosis, name = 'reportDiagnosis'),
	path('rprt_App_Count_Doctor/', views.rprt_App_Count_Doctor, name = 'rprt_App_Count_Doctor'),
	path('rprt_App_Count_Clinic/', views.rprt_App_Count_Clinic, name = 'rprt_App_Count_Clinic'),
	path('rprt_App_Status_Today/', views.rprt_App_Status_Today, name = 'rprt_App_Status_Today'),
	path('rprt_CD_Details/', views.rprt_CD_Details, name = 'rprt_CD_Details'),
	path('rprt_alrgic_med/', views.rprt_alrgic_med, name = 'rprt_alrgic_med'),
	path('rprt_mst_recmd_med/', views.rprt_mst_recmd_med, name = 'rprt_mst_recmd_med'),
	path('rprt_CD_Cunt_dctr/', views.rprt_CD_Cunt_dctr, name = 'rprt_CD_Cunt_dctr'),
	path('rprt_total_pymnt/', views.rprt_total_pymnt, name = 'rprt_total_pymnt'),
	path('rprt_Emp_Cunt_By_Desig/', views.rprt_Emp_Cunt_By_Desig, name = 'rprt_Emp_Cunt_By_Desig'),
	path('rprt_Ptnt_Htry/', views.rprt_Ptnt_Htry, name = 'rprt_Ptnt_Htry'),
	path('rprt_Sytm_Htry/', views.rprt_Sytm_Htry, name = 'rprt_Sytm_Htry'),
	
	path('userdetails/', views.userdetails, name = 'userdetails'),
	


	path('register/', views.registerpage, name = 'register'),
	path('login/', views.loginpage, name = 'login'),
	path('login2/', views.loginpage2, name = 'login2'),
	path('logout/', views.logoutuser, name = 'logout'),
	path('dashboard/', views.dashboard, name = 'dashboard'),

	
	re_path(r'^employees/(?P<pk>\d+)?$', views.employee, name = 'employees'),



	re_path(r'^clinics/(?P<pk>\d+)?$', views.clinic, name = 'clinics'),
	# re_path(r'^clinics/', permission_required('appsample.add_clinic', login_url='login')('clinics')),

	

	re_path(r'^clinicDates/(?P<pk>\d+)?$', views.clinicDate, name = 'clinicDates'),

	re_path(r'^patients/(?P<pk>\d+)?$', views.patient, name = 'patients'),
		
	re_path(r'^designations/(?P<pk>\d+)?$', views.designation, name = 'designations'),

	re_path(r'^diagnosises/(?P<pk>\d+)?$', views.diagnosis, name = 'diagnosises'),

	re_path(r'^diagnosissymtoms/(?P<pk>\d+)?$', views.diagnosissymtom, name = 'diagnosissymtoms'),

	re_path(r'^symptoms/(?P<pk>\d+)?$', views.symptom, name = 'symptoms'),

	re_path(r'^appointments/(?P<pk>\d+)?$', views.appointment, name = 'appointments'),

	re_path(r'^appointments1/(?P<pk>\d+)?$', views.appointment1, name = 'appointments1'),

	re_path(r'^appointment2/(?P<pk>\d+)?$', views.appointment2, name = 'appointment2'),

	path('api/clinic_date/', views.load_clinic_date, name='clinic_date'),
	path('api/designation_employees/', views.load_designation_employees, name='designation_employees'),
	path('api/appoinment_numbers/', views.load_appoinment_numbers, name='appoinment_numbers'),
	path('api/diagnosis/', views.load_diagnosis, name='diagnosis'),
	path('api/load_symtoms/', views.load_symtoms, name='load_symtoms'),
	path('api/total/', views.total, name='total'),
	
	re_path(r'^api/clinic_date_details/(?P<pk>\d+)$', views.load_clinic_date_details, name='clinic_date_details'),
	# re_path(r'^api/clinicdetails/(?P<pk>\d+)$', views.load_clinicdetails, name='clinic_clinicdetails'),
	re_path(r'^api/appointment_details/(?P<pk>\d+)$', views.load_appointment_details, name='appointment_details'),
	re_path(r'^api/doctor_clinic_date/', views.load_doctor_clinic_date, name='doctor_clinic_date'),

	re_path(r'^prescriptions/(?P<pk>\d+)?$', views.prescription, name = 'prescriptions'),

	re_path(r'^appointmentDiagnosis/(?P<pk>\d+)?$', views.appointmentDiagnosis, name = 'appointmentDiagnosis'),

	re_path(r'^appointmentSymptoms/(?P<pk>\d+)?$', views.appointmentSymptom, name = 'appointmentSymptoms'),

	re_path(r'^rooms/(?P<pk>\d+)?$', views.room, name = 'rooms'),

	re_path(r'^services/(?P<pk>\d+)?$', views.service, name = 'services'),

	re_path(r'^invoices/(?P<pk>\d+)?$', views.invoice, name = 'invoices'),

	re_path(r'^payments/(?P<pk>\d+)?$', views.payment, name = 'payments'),

	re_path(r'^invoiceservices/(?P<pk>\d+)?$', views.invoiceservice, name = 'invoiceservices'),

	re_path(r'^appoinmentstatus/(?P<pk>\d+)?$', views.appoinmentstatus, name = 'appoinmentstatus'),

	re_path(r'^medicines/(?P<pk>\d+)?$', views.medicine, name = 'medicines'),




	path('test1/',views.test1),
	path('test2/',views.test2),
	path('test3/',views.test3),
	path('test4/',views.test4),

]



	# path('appoinmentstatus/', views.appoinmentstatus, name = 'appoinmentstatus'),
	# path('update_appoinmentstatus/<str:pk>', views.updateappoinmentstatus, name = 'update_appoinmentstatus'),
	# path('deleteappoinmentstatus/<str:pk>', views.deleteappoinmentstatus, name = 'deleteappoinmentstatus'),