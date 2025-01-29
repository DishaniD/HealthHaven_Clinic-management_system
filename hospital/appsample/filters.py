import django_filters 
from .models import *
from django.forms.widgets import Select, DateInput, TextInput, DateTimeInput


class EmployeeFilter(django_filters.FilterSet):
	user = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'User Name'}))
	designation = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Designation'}))
	mobile1 = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Contact Number'}))
	mobile2 = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Contact Number'}))
	nic = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'search nic'}))

	class Meta:
		model = Employee
		exclude = ['photo', 'dob', 'address', 'slmc_no', 'etf_no', 'civilStatus', 'gender']

class ClinicFilter(django_filters.FilterSet):
	name = django_filters.CharFilter( widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Clinic name'}))
	room = django_filters.CharFilter( widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Room number'}))
	
	class Meta:
		model = Clinic
		fields = '__all__' 

class ClinicDateFilter(django_filters.FilterSet):
	capacity = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'capacity'}))
	start_time = django_filters.CharFilter(lookup_expr='icontains', widget= DateTimeInput(attrs = {'class':'form-control', 'placeholder':'start_time', 'type':'Datetime-local'}))
	class Meta:
		model = ClinicDate
		fields = '__all__' 

class PatientFilter(django_filters.FilterSet):
	first_name = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Patient name'}))
	mobile1 = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Contact Number'}))
	nic = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'search nic'}))

	class Meta:
		model = Patient
		fields = '__all__' 

class DesignationFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Designation'}))
	class Meta:
		model = Designation
		fields = '__all__' 

class DiagnosisFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Diagnosis
		fields = '__all__' 

class DiagnosisSymptomFilter(django_filters.FilterSet):
	class Meta:
		model = DiagnosisSymptom
		fields = '__all__' 
		
class SymptomFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Symptom
		fields = '__all__' 

class PrescribeFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Prescribe
		fields = '__all__' 

class AppointmentFilter(django_filters.FilterSet):
	appointmentnumber = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Enter appoinment'}))
	first_name = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'patient name'}))
	clinic_date = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'yyyy-mm-dd'}))
	class Meta:
		model = Appointment
		fields = '__all__' 

class AppointmentFilter1(django_filters.FilterSet):
	appointmentnumber = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'Enter appoinment'}))
	first_name = django_filters.CharFilter(field_name='patient__first_name', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'patient name'}))
	clinic_date = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'yyyy-mm-dd'}))
	class Meta:
		model = Appointment
		fields = '__all__' 

class PrescriptionFilter(django_filters.FilterSet):
	class Meta:
		model = Prescription
		fields = '__all__'

class AppointmentDiagnosisFilter(django_filters.FilterSet):
	class Meta:
		model = AppointmentDiagnosis
		fields = '__all__'

class AppointmentSymptomFilter(django_filters.FilterSet):
	class Meta:
		model = Appointmentsymptom
		fields = '__all__'

class RoomFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Room
		fields = '__all__' 

class ServiceFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains', widget= TextInput(attrs = {'class':'form-control', 'placeholder':'service'}))
	class Meta:
		model = Service
		fields = '__all__' 

class InvoiceFilter(django_filters.FilterSet):
	reference_no = django_filters.CharFilter(lookup_expr='icontains')
	appointment = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Invoice
		fields = '__all__' 

class PaymentFilter(django_filters.FilterSet):
	payment = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Payment
		fields = '__all__' 

class InvoiceServiceFilter(django_filters.FilterSet):
	class Meta:
		model = InvoiceService
		fields = '__all__' 

class AppoinmentStatusFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = AppoinmentStatus
		fields = '__all__' 

class MedicineFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Medicine
		fields = '__all__'