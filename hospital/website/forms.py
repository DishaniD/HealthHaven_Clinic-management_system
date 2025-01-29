from django.forms import ModelForm, ModelChoiceField, CharField
from appsample.models import *
from appsample.forms import *
from django.forms.widgets import Select, DateInput, TextInput, CheckboxSelectMultiple, NumberInput, DateTimeInput, Textarea
from django.core.exceptions import ValidationError
import re


class NewsForm(ModelForm):
	class Meta:
		model = News
		exclude = ['readers', 'created_by' ]
		widgets = { 
			
			'title':TextInput(attrs = {'class':'form-control', 'placeholder':'Write the Tittle'}), 
			'description':Textarea(attrs = {'class':'form-control', 'placeholder':'Enter Description'}),
			#'created_by':TextInput(attrs = {'class':'form-control'}),	
		}

class NewsForm2(ModelForm):
	class Meta:
		model = News
		exclude = ['readers', 'created_by' ]
		widgets = { 
			
			'title':TextInput(attrs = {'class':'form-control', 'placeholder':'Write the Tittle'}), 
			'description':Textarea(attrs = {'class':'form-control', 'placeholder':'Enter Description'}),
			#'created_by':TextInput(attrs = {'class':'form-control'}),	
		}


class AppointmentForm(ModelForm):
	clinic = ModelChoiceField(queryset = Clinic.objects.all(), widget= Select(attrs = {'class':'form-select', 'placeholder':'Select Clinic'}))
	class Meta:
		model = Appointment
		fields = '__all__'
		widgets = { 

			'appointmentnumber':TextInput(attrs = {'class':'form-control', 'placeholder':'Select a Clinic Date', 'disabled':''}),
			'patient':Select(attrs = {'class':'form-select'}),
			'clinic_date':Select(attrs = {'class':'form-select', 'placeholder':'Select Date', 'disabled':''}),
			'symptoms': CheckboxSelectMultiple(attrs={}),
			'diagnosis': Select(attrs = {'class':'form-select'}),
			'medicines': CheckboxSelectMultiple(attrs={}),
           			
		}

class patientAccountForm(ModelForm):
	clinic = ModelChoiceField(queryset = Clinic.objects.all(), widget= Select(attrs = {'class':'form-control col-md-12', 'placeholder':'Select Clinic'}))
	class Meta:
		model = Appointment
		fields = '__all__'
		exclude = ['diagnosis', 'medicines', 'invoice', 'appoinment_status', 'patient']
		widgets = { 

			'appo_no':TextInput(attrs = {'class':'form-control col-md-12'}),
			'clinic_date':Select(attrs = {'class':'form-control col-md-12'}),
			'doctor':Select(attrs = {'class':'form-control col-md-12'}),
			'patient':Select(attrs = {'class':'form-control col-md-12'}),
           			
		}

class AppointmentForm2(ModelForm):
	clinic = ModelChoiceField(queryset = Clinic.objects.all(), widget= Select(attrs = {'class':'form-select', 'placeholder':'Select Clinic', 'readonly':'readonly'}))
	class Meta:
		model = Appointment
		fields = '__all__'
		exclude = ['medicines', 'invoice', 'appoinment_status']
		widgets = { 

			'appo_no':TextInput(attrs = {'class':'form-control'}),
			'clinic_date':Select(attrs = {'class':'form-select'}),
			'doctor':Select(attrs = {'class':'form-select'}),
			'diagnosis':Select(attrs = {'class':'form-select'}),
			'patient':Select(attrs = {'class':'form-select'}),
           			
		}
class InvoiceForm2(ModelForm):
	class Meta:
		model = Invoice
		fields = ['appointment_fee']
		# exclude = ['services']
		widgets = { 
			
			'reference_no':TextInput(attrs = {'class':'form-control', 'placeholder':'reference_no'}), 
			'appointment_fee':NumberInput(attrs = {'class':'form-control', 'placeholder':'1000', 'readonly':'readonly'}),
			'discount':NumberInput(attrs = {'class':'form-control', 'placeholder':'discount'}),
			'doctor_fee':NumberInput(attrs = {'class':'form-control', 'placeholder':'doctor fee'}),

		}