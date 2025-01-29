from django.forms import ModelForm, ModelChoiceField, CharField, ImageField, DecimalField
from django.db.models import PositiveIntegerField
from .models import *
from django.forms.widgets import Select, DateInput, TextInput, CheckboxSelectMultiple, NumberInput, DateTimeInput, FileInput
from django.core.exceptions import ValidationError
import re

class EmployeeForm(ModelForm):
	photo:ImageField(widget=FileInput(attrs={'onchange': 'mpreview();'}))
	class Meta:
		model = Employee
		exclude = ['user']
		widgets = { 
			'first_name':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter First Name'}),
			'second_name':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Middle Name'}),
			'email':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Email'}),
			'dob':DateInput(attrs = {'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
			'mobile1':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Contact'}),
			'mobile2':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Contact 2'}),
			'designation':Select(attrs = {'class':'form-select', 'placeholder':'Insert the Designation'}),
			'address':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Address'}),
			'slmc_no':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert SLMC NO'}),
			'etf_no':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert ETF NO'}),
			'nic':TextInput(attrs = {'class':'form-control nic-validate', 'placeholder':'Enter NIC'}),
			'nameTitle':Select(attrs = {'class':'form-select', 'placeholder':'select the user'}),
			'civilStatus':Select(attrs = {'class':'form-select', 'placeholder':'select the user'}),
			'gender':TextInput(attrs = {'class':'form-control', 'placeholder':'select the user'}),
			'fee':NumberInput(attrs = {'class':'form-control'}),
			
           			
		}
	def clean_nic(self):
		nic = self.cleaned_data['nic']
		if not re.search('^(?:19|20)?\d{2}[0-9]{10}|[0-9]{9}[x|X|v|V]$', nic):
			raise ValidationError('enter correct nic')
		return nic		

class ClinicForm(ModelForm):
	class Meta:
		model = Clinic
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Contact'}), 
			'designation':Select(attrs = {'class':'form-control', 'placeholder':'Insert the Doctor'}),
			'room':Select(attrs = {'class':'form-control', 'placeholder':'Insert the Room Num'}),	
		}

class ClinicDateForm(ModelForm):
	class Meta:
		model = ClinicDate
		fields = '__all__'
		widgets = { 
			
			'start_time':DateTimeInput(attrs = {'class':'form-control ', 'placeholder':'yyyy-mm-dd', 'type':'Datetime-local'}), #, 'min':'2022-06-01T08:30'
			'doctor':Select(attrs = {'class':'form-select', 'disabled':''}),
			'nurse':Select(attrs = {'class':'form-select' }),
			'clinic':Select(attrs = {'class':'form-select', 'placeholder':'Insert the Clinic'}),
			'capacity':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter capacity'}),
			'currentno':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter currentno'}),
			'occupied':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter occupied'}),
           			
		}

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		exclude = ['user']
		widgets = { 
			'first_name':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Middle Name'}),
			'second_name':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Middle Name'}),
			'age':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Age'}),
			'nic':TextInput(attrs = {'class':'form-control nic-validate', 'placeholder':'Enter NIC'}),
			'gender':TextInput(attrs = {'class':'form-control', 'placeholder':'select the user'}),
			'dob':DateInput(attrs = {'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
			'mobile1':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Contact'}),
			'address':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Address'}),
			'email':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Address'}),
			'loyalty':Select(attrs = {'class':'form-control', 'placeholder':'loyalty', 'disabled':''}),
			
		}
	def clean_contact(self):
		mobile1 = self.cleaned_data['mobile1']
		if not re.search('^0\d{9}$', mobile1):
			raise ValidationError('enter correct mobile number')
		return contact


class DesignationForm(ModelForm):
	class Meta:
		model = Designation
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Designation'}),
           			
		}

class DiagnosisForm(ModelForm):
	class Meta:
		model = Diagnosis
		exclude = ['symptoms']
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Diagnosis'}),
			'dprobability':NumberInput(attrs = {'class':'form-control', 'placeholder':'Diagnosis probability', 'min':0, 'max':1}),
			#'symptom': Select(attrs = {'class':'form-select'}),
			#'probability': NumberInput(attrs = {'class':'form-control', 'placeholder':'Insert the probability', 'min':0, 'max':1}),

           			
		}

class SymptomForm(ModelForm):
	class Meta:
		model = Symptom
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Symptom'}),
			'probability':NumberInput(attrs = {'class':'form-control', 'placeholder':'Insert the probability', 'min':0, 'max':1}),
           	
		}

class DiagnosisSymptomForm(ModelForm):
	class Meta:
		model = DiagnosisSymptom
		fields = '__all__'
		widgets = { 
			
			'probability':NumberInput(attrs = {'class':'form-control', 'placeholder':'Insert the probability'}),
           	#'symptom': CheckboxSelectMultiple(attrs={}),
		}


class MedicineForm(ModelForm):
	class Meta:
		model = Medicine
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter medicines'}), 
				
		}

class AppointmentForm(ModelForm):
	clinic = ModelChoiceField(queryset = Clinic.objects.all(), widget= Select(attrs = {'class':'form-select', 'placeholder':'Select Clinic'}))
	class Meta:
		model = Appointment
		fields = '__all__'
		widgets = { 

			'appo_no':TextInput(attrs = {'class':'form-control', 'placeholder':'Select a Clinic Date', 'disabled':''}),
			'patient':Select(attrs = {'class':'js-example-basic-single col-sm-12', 'name':'state'}),
			'clinic_date':Select(attrs = {'class':'form-select', 'placeholder':'Select Date', 'disabled':''}),
			'symptoms': CheckboxSelectMultiple(attrs={}),
			'diagnosis': Select(attrs = {'class':'form-select'}),
			'medicines': CheckboxSelectMultiple(attrs={}),
           			
		}

class AppointmentForm1(ModelForm):
	clinic = ModelChoiceField(queryset = Clinic.objects.all(), widget= Select(attrs = {'class':'form-select', 'placeholder':'Select Clinic'}))
	class Meta:
		model = Appointment
		fields = '__all__'
		exclude = ['diagnosis', 'medicines', 'invoice']
		widgets = { 

			'appo_no':TextInput(attrs = {'class':'form-control', 'placeholder':'appoinment Number'}),
			'patient':Select(attrs = {'class':'js-example-basic-single col-sm-12', 'name':'state'}),
			'clinic':Select(attrs = {'class':'form-select'}),
			'doctor':Select(attrs = {'class':'form-select'}),
			'clinic_date':Select(attrs = {'class':'form-select', 'placeholder':'Select Date'}),
			'appoinment_status':Select(attrs = {'class':'form-select'}),
			
           			
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

class PrescriptionForm(ModelForm):
	class Meta:
		model = Prescription
		fields = '__all__'
		widgets = { 
			'description':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Description'}),
			'medicine':Select(attrs = {'class':'form-select'}),
			'frequency':Select(attrs = {'class':'form-select'}),
			'unit':Select(attrs = {'class':'form-select'}),
			'appointment':Select(attrs = {'class':'form-select'}),
			'morning':NumberInput(attrs = {'class':'form-control', 'placeholder':' Number of Units'}),
			'noon':NumberInput(attrs = {'class':'form-control', 'placeholder':' Number of Units'}),
			'evening':NumberInput(attrs = {'class':'form-control', 'placeholder':' Number of Units'}),
			'night':NumberInput(attrs = {'class':'form-control', 'placeholder':' Number of Units'}),
			'duration':NumberInput(attrs = {'class':'form-control', 'placeholder':' Days'}),

		}

class AppointmentDiagnosisForm(ModelForm):
	class Meta:
		model = AppointmentDiagnosis
		fields = '__all__'
		widgets = { 
			'appointment':Select(attrs = {'class':'form-select'}),
			'diagnosis':Select(attrs = {'class':'form-select'}),
           			
		}

class AppointmentSymptomForm(ModelForm):
	class Meta:
		model = Appointmentsymptom
		fields = '__all__'
		widgets = { 
			'appointment':Select(attrs = {'class':'form-select'}),
			'symptom':Select(attrs = {'class':'form-select'}),
           			
		}

class RoomForm(ModelForm):
	class Meta:
		model = Room
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control ', 'placeholder':'Insert the Room Name'}),   			
		}

	def clean_name(self):
		name = self.cleaned_data['name']
		if name != 'abc':
			raise ValidationError('Not abc')
		return name

class ServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Service'}),
			'charge':NumberInput(attrs = {'class':'form-control', 'placeholder':'Charge'}),  
						
		}


class InvoiceForm(ModelForm):
	#total = DecimalField(max_digits=8, decimal_places=2, widget= NumberInput( attrs = {'class':'form-control', 'placeholder':'Total', 'readonly':''}))
	class Meta:
		model = Invoice
		# fields = '__all__'
		exclude = ['services']
		widgets = { 
			
			'reference_no':TextInput(attrs = {'class':'form-control', 'placeholder':'reference_no', 'readonly':''}), 
			'appointment_fee':NumberInput(attrs = {'class':'form-control', 'placeholder':'appointment fee'}),
			'discount':NumberInput(attrs = {'class':'form-control', 'placeholder':'discount'}),
			'doctor_fee':NumberInput(attrs = {'class':'form-control', 'placeholder':'doctor fee', 'readonly':''}),
			'appointment':Select(attrs = {'class':'form-select'}),
			'discounted_total':NumberInput(attrs = {'class':'form-control', 'placeholder':'Total', 'readonly':''}),




		}

class InvoiceForm2(ModelForm):
	class Meta:
		model = Invoice
		# fields = '__all__'
		fields = ['appointment_fee']
		widgets = { 
			'appointment_fee':NumberInput(attrs = {'class':'form-control', 'placeholder':'appointment fee'}),
		}

class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields = '__all__'
		widgets = { 
			
			'payment':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Payment'}), 
			'invoice':Select(attrs = {'class':'form-select'}),
			'amount':NumberInput(attrs = {'class':'form-control ', 'placeholder':'amount'}),
			'balance':NumberInput(attrs = {'class':'form-control ', 'placeholder':'balance'}),
			'date':DateInput(attrs = {'class':'form-control ', 'placeholder':'yyyy-mm-dd'}), #, 'min':'2022-06-01T08:30'  			
		}

class InvoiceServiceForm(ModelForm):
	class Meta:
		model = InvoiceService
		exclude = ['appointment']
		widgets = { 
			
			'service':Select(attrs = {'class':'form-select '}),	
			'description':TextInput(attrs = {'class':'form-control', 'placeholder':'description'}),
			'multiple':NumberInput(attrs = {'class':'form-control ', 'placeholder':'multiple'}),			
		}

class AppoinmentStatusForm(ModelForm):
	class Meta:
		model = AppoinmentStatus
		fields = '__all__'
		widgets = { 
			
			'name':TextInput(attrs = {'class':'form-control', 'placeholder':'Enter Status'}),			
		}

