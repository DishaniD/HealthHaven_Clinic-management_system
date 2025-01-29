from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Designation(models.Model):
	name = models.CharField(max_length = 255)
	
	def __str__ (self):  
		return self.name

class Gender(models.Model):
	name = models.CharField(max_length = 15)
	
	def __str__ (self):  
		return self.name

class CivilStatus(models.Model):
	name = models.CharField(max_length = 255)
	
	def __str__ (self):  
		return self.name

class NameTitle(models.Model):
	name = models.CharField(max_length = 255)
	
	def __str__ (self):  
		return self.name


class Employee(models.Model):
	photo = models.ImageField(null=True, blank=True, upload_to='appsample/profile_photos')
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
	nameTitle = models.ForeignKey(NameTitle, on_delete=models.CASCADE)
	first_name = models.CharField(max_length = 100, validators=[RegexValidator(regex='^\w+$', message='name cannot contain symbles and spaces')])
	second_name = models.CharField(max_length = 100, validators=[RegexValidator(regex='^\w+$', message='name cannot contain symbles and spaces')])
	nic = models.CharField(max_length = 12, validators=[RegexValidator(regex=r'^(?:19|20)?\d{2}[0-9]{10}|[0-9]{9}[x|X|v|V]$', message='Enter Correct NIC ')])
	dob = models.DateField()
	gender = models.CharField(max_length = 10)
	mobile1 = models.CharField(max_length = 10)
	mobile2 = models.CharField(max_length = 10)
	email = models.TextField()
	civilStatus = models.ForeignKey(CivilStatus, on_delete=models.CASCADE,)
	etf_no = models.CharField(max_length = 10, null=True, blank=True,)
	designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
	slmc_no = models.CharField(max_length = 10, null=True, blank=True,)
	address = models.TextField()
	fee= models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,)
	

	def __str__ (self):  # java wla tooltip wage
		return self.user.username

class Clinic(models.Model):
	name = models.CharField(max_length = 255)
	designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True,)
	

	def __str__ (self): 
		return self.name

class Room(models.Model):
	name = models.CharField(max_length = 20)
	
	def __str__ (self): 
		return self.name
	
class ClinicDate(models.Model):
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name = 'clinic_dates_as_doctor')
	nurse = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name ='clinic_dates_as_nurse')
	capacity = models.IntegerField( null=True, blank=True,)
	start_time =models.DateTimeField(null=True)
	currentno = models.IntegerField( null=True, blank=True,)
	occupied = models.IntegerField( null=True, blank=True,)
	#room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True,)
	
	
	def __str__ (self):  
		return self.clinic.name + '_' + str(self.doctor) + '_' + str(self.start_time)

class Medicine(models.Model):
	name = models.CharField(max_length = 200)
	

	def __str__ (self): 
		return self.name

class Loyalty(models.Model):
	name = models.CharField(max_length = 255)
	minimum_appointment = models.IntegerField(null=True, blank=True)
	discount = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

	def __str__ (self): 
		return self.name

class Patient(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True )
	first_name = models.CharField(max_length = 100, validators=[RegexValidator(regex='^\w+$', message='name cannot contain symbles')])
	second_name = models.CharField(max_length = 100, validators=[RegexValidator(regex='^\w+$', message='name cannot contain symbles')])
	nic = models.CharField(max_length = 12, null=True, blank=True)
	dob = models.DateField()
	gender = models.CharField(max_length = 10)
	age = models.IntegerField()
	address = models.TextField( validators=[RegexValidator(regex='^[#.0-9a-zA-Z\s,-]+$', message='Please enter correct address')] )
	email = models.TextField()
	mobile1 = models.CharField(max_length = 10,)
	allergies = models.ManyToManyField(Medicine, blank=True)
	loyalty = models.ForeignKey(Loyalty, on_delete=models.CASCADE, default=1, blank=True)

	
	def __str__ (self): 
		return self.first_name

class AppoinmentStatus(models.Model):
	name = models.CharField(max_length = 20)
	
	def __str__ (self): 
		return self.name


class Symptom(models.Model):
	name = models.CharField(max_length = 100)
	probability= models.DecimalField(max_digits=3, decimal_places=2, null=True)
	
	def __str__ (self):  
		return self.name

class Diagnosis(models.Model):
	name = models.CharField(max_length = 20)
	dprobability = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	symptoms = models.ManyToManyField(Symptom, through='DiagnosisSymptom')

	
	def __str__ (self):  
		return self.name

class DiagnosisSymptom(models.Model):
	symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
	diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
	probability = models.DecimalField(max_digits=3, decimal_places=2, null=True)

	class Meta:
		db_table = 'appsample_diagnosis_symptoms'
		unique_together = ('diagnosis', 'symptom')

	
	def __str__ (self):  
		return "%s %s" % (self.symptom, self.diagnosis)


class Prescribe(models.Model):
	name = models.CharField(max_length = 20)
	
	def __str__ (self):  
		return self.name

class Service(models.Model):
	name = models.CharField(max_length = 255)
	charge = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	
	def __str__ (self): 
		return self.name



class Appointment(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, related_name = 'appointment_as_doctor')
	clinic_date = models.ForeignKey(ClinicDate, on_delete=models.CASCADE)
	appo_no = models.CharField(max_length = 20, null=True)
	appoinment_status = models.ForeignKey(AppoinmentStatus, on_delete=models.CASCADE, default=1)
	 #invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
	symptoms = models.ManyToManyField(Symptom, blank=True)
	diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, null=True, blank=True)
	medicines = models.ManyToManyField(Medicine, blank=True)

	
	def __str__ (self):  
		return self.appo_no + '_' + str(self.clinic_date.start_time) + '_' + str(self.patient) + '_' + str(self.doctor)

	class Meta:
		permissions = [
			('view_doctor', 'Can view doctors appointments'),
			# ('view_future', 'Can view all future appointments'), 
		]

			

class Invoice(models.Model):
	appointment = models.OneToOneField(Appointment, primary_key=True, on_delete=models.CASCADE)
	reference_no = models.CharField(max_length = 20)
	appointment_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	doctor_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	discount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	discounted_total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	services = models.ManyToManyField(Service, through='InvoiceService')
	
	def __str__ (self): 
		return self.reference_no + '_' + str(self.appointment.patient.first_name)

class InvoiceService(models.Model):
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	multiple = models.PositiveIntegerField(default=1, blank=True)
	description = models.CharField(max_length = 400, null=True, blank=True)

	def __str__ (self):  
		return "%s %s" % (self.invoice, self.service)

	class Meta:
		db_table = 'appsample_invoiceservice'
		unique_together = ('invoice', 'service')

class AppointmentDiagnosis(models.Model):
	diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
		
	def __str__ (self):  
		return self.name + '_' + str(self.appointment)

class Appointmentsymptom(models.Model):
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
	symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
	
	def __str__ (self):
		return str(self.appointment) + '_' + str(self.symptom) 

class Payment(models.Model):
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	date = models.DateField(null=True, blank=True)
	amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	balance =models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

	def __str__ (self): 
		return self.invoice

class Frequency(models.Model):
	name = models.CharField(max_length = 20)

	def __str__ (self): 
		return self.name

class Unit(models.Model):
	name = models.CharField(max_length = 20)

	def __str__ (self): 
		return self.name

class Prescription(models.Model):
	# patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	# clinicDate = models.ForeignKey(ClinicDate, on_delete=models.CASCADE, null=True, blank=True)
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
	medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True)
	frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE, null=True)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
	morning = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
	noon = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
	evening = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
	night = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
	duration = models.DecimalField(max_digits=4, decimal_places=0, null=True)
	description = models.CharField(max_length = 30, null=True, blank=True)
	# route = models.CharField(max_length = 30, null=True, blank=True)


	def __str__ (self):  
		return self.medicine.name


class News(models.Model):
    title = models.CharField(max_length = 500, null=True, blank=True)
    description = models.CharField(max_length = 5000, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    readers = models.ManyToManyField(User)
 
    def __str__ (self):        
        return self.title

class News2(models.Model):
    title = models.CharField(max_length = 500, null=True, blank=True)
    description = models.CharField(max_length = 5000, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    readers = models.ManyToManyField(User)
 
    def __str__ (self):        
        return self.title


