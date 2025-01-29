from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .filters import *
from .decorators import unauthenticated_user, allowed_users, permission, unauthenticated_user2
from django.forms import inlineformset_factory
from django.forms.widgets import TextInput
from django.contrib import messages
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
import json
from django.db.models import Count, Avg, Q
from django.db.models import Max
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission
from datetime import datetime
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
# Create your views here. reportAppointments

def reportDiagnosis (request):
	diagnosises = Diagnosis.objects.all() 

	context = {'diagnosises':diagnosises}
	return render(request, 'reportDiagnosis.html', context)

def rprt_Emp_Cunt_By_Desig (request):
	designations = Designation.objects.annotate(num_employees=Count('employee'))\
		.annotate(num_male_emp=Count('employee', filter=Q(employee__gender='Male')))\
		.annotate(num_female_emp=Count('employee', filter=Q(employee__gender='Female')))

	context = {'designations':designations}
	return render(request, 'rprt_Emp_Cunt_By_Desig.html', context)

def rprt_Ptnt_Htry (request):
	patients = Patient.objects.all()
	diagnosises = Diagnosis.objects.annotate(num_appoint=Count('appointment'))
	selected_patient = 0

	if 'patient' in request.GET:
		selected_patient = int(request.GET['patient'])
		diagnosises = Diagnosis.objects.annotate(num_appoint=Count('appointment', filter=Q(appointment__patient=selected_patient)))

	context = {'patients':patients, 'selected_patient':selected_patient, 'diagnosises':diagnosises}
	return render(request, 'rprt_Ptnt_Htry.html', context)

def rprt_Sytm_Htry (request):
	symts = Symptom.objects.all()
	diagnosises = Diagnosis.objects.annotate(num_appoint=Count('appointment'))
	selected_symptom = 0

	if 'symptom' in request.GET:
		selected_symptom = int(request.GET['symptom'])
		diagnosises = Diagnosis.objects.annotate(num_appoint=Count('appointment', filter=Q(appointment__symptoms=selected_symptom)))


	context = {'symts':symts, 'selected_symptom':selected_symptom, 'diagnosises':diagnosises}
	return render(request, 'rprt_Sytm_Htry.html', context)

def rprt_App_Count_Doctor (request):
	clinics = Clinic.objects.all()
	clinicDates = ClinicDate.objects.all()

	context = {'clinics':clinics, 'clinicDates':clinicDates}
	return render(request, 'rprt_App_Count_Doctor.html', context)

def rprt_App_Count_Clinic (request):
	clinics = Clinic.objects.annotate(avg_occupied=Avg('clinicdate__occupied'))


	context = {'clinics':clinics}
	return render(request, 'rprt_App_Count_Clinic.html', context)

def rprt_App_Status_Today (request):
	clinics = Clinic.objects.all()
	clinicDates = ClinicDate.objects.all()

	context = {'clinics':clinics, 'clinicDates':clinicDates}
	return render(request, 'rprt_App_Status_Today.html', context)

def rprt_CD_Details (request):
	clinics = Clinic.objects.all()
	clinicDates = ClinicDate.objects.all()

	context = {'clinics':clinics, 'clinicDates':clinicDates}
	return render(request, 'rprt_CD_Details.html', context)

def rprt_alrgic_med (request):  #manay to many table issue

	context = {}
	return render(request, 'rprt_alrgic_med.html', context)

def rprt_mst_recmd_med (request):
	clinics = Clinic.objects.all()

	context = {'clinics':clinics}
	return render(request, 'rprt_mst_recmd_med.html', context)

def rprt_CD_Cunt_dctr (request):
	clinics = Clinic.objects.all()

	context = {'clinics':clinics}
	return render(request, 'rprt_CD_Cunt_dctr.html', context)

def rprt_total_pymnt (request):

	context = {}
	return render(request, 'rprt_total_pymnt.html', context)
	
def contacts (request):
	context = {'name':'Disani', 'town':'Kandy'}
	return render(request, 'contacts.html', context)

def customer (request):
	context = {'name':'Sithara', 'town':'Kandy'}
	return render(request, 'customer.html', context)	
	
def products (request):
	context = {'name':'Hasanga', 'town':'Kandy'}
	return render(request, 'products.html', context)	
	
def registerpage (request):

	if request.POST:
		form = PatientForm(request.POST)
		userform = UserCreationForm(request.POST)

		if form.is_valid() and userform.is_valid():
			messages.success(request, "Successfully registered")
			userobj = userform.save()
			patient_group = Group.objects.get(name='Patient') 
			patient_group.user_set.add(userobj)
			patient_group.save()
			obj = form.save(commit=False)
			obj.user = userobj
			form.save()
			return redirect('login')

	else:
		form = PatientForm()
		userform = UserCreationForm()

	context = {'form':form, 'userform':userform}
	return render(request, 'register.html', context)


@unauthenticated_user	
def loginpage (request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username = username, password = password)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('patientaccount')
			else:
				return HttpResponse("Disable account")

		else:
			messages.error(request, "Invalid Login")
	else:
		pass
		
	context ={}
	return render(request, 'login.html', context)

@unauthenticated_user2	
def loginpage2 (request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username = username, password = password)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('dashboard')
			else:
				return HttpResponse("Disable account")

		else:
			messages.error(request, "Invalid Login")
	else:
		pass
		
	context ={}
	return render(request, 'login.html', context)

def logoutuser (request):
	logout (request)
	return redirect ('home')
	

@allowed_users(roles = ['Receptionist', 'Doctor', 'Nurse', 'Manager', 'Cashier', 'Admin'])
#@has_perm('appsample.view_doctor')
def dashboard (request):
	# data = Appointment.objects.all()

	if request.user.has_perm('appsample.view_doctor'):
		data= Appointment.objects.filter(doctor__user=request.user).filter(clinic_date__start_time__date = datetime.today()).count()

	context = {'data':data}
	return render(request, 'dashboard.html', context)	

@allowed_users(roles = ['Manager'])
def employee(request, pk=None):
	model = Employee.objects.get(pk=pk) if pk else Employee()
	data = Employee.objects.all()

	data_paginator = Paginator(data, 100)	
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)

	filter = EmployeeFilter(request.GET, queryset = data)
	data = filter.qs
	
	if request.POST.get('save'):
		form = EmployeeForm(request.POST, instance=model)
		userform = UserCreationForm(request.POST)

		if form.is_valid() and userform.is_valid():
			messages.success(request, "Add Successfully")
			userobj = userform.save()
			obj = form.save(commit=False)
			obj.user = userobj
			try:	
				patient_group = Group.objects.get(name=obj.designation.name)
			except Group.DoesNotExist:
				patient_group = Group.objects.get(name='Doctor')
			patient_group.user_set.add(userobj)
			patient_group.save()
			form.save()
			return redirect('/appsample/employees')

	else:
		form = EmployeeForm(instance=model)
		userform = UserCreationForm()

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/appsample/employees')

	context = {'form':form, 'filter':filter, 'page':page, 'userform':userform}
	return render(request, 'employee.html', context)


@allowed_users(roles = ['Manager'])
# @permission('appsample.add_clinic')
def clinic(request, pk=None):
	model = Clinic.objects.get(pk=pk) if pk else Clinic()
	data = Clinic.objects.all()
	

	data_paginator = Paginator(data, 100)
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)

	filter = ClinicFilter(request.GET, queryset = data)
	data = filter.qs
	
	if request.POST.get('save'):
		# print("hello")
		form = ClinicForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			messages.success(request, "Add Successfully")
			news = News(title = request.POST.get('name'), description = request.POST.get('designation'), created_by = request.user)
			news.save()
			return redirect('/appsample/clinics')

	else:
		form = ClinicForm(instance=model)

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/appsample/clinics')

	context = {'form':form, 'filter':filter, 'page':page}
	return render(request, 'clinic.html', context)



@allowed_users(roles = ['Receptionist', 'Doctor', 'Manager'])
def clinicDate(request, pk=None):
	model = ClinicDate.objects.get(pk=pk) if pk else ClinicDate()
	data = ClinicDate.objects.all()

	filter = ClinicDateFilter(request.GET, queryset = data)
	data = filter.qs

	data_paginator = Paginator(data, 100)	
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)
	
	if request.POST.get('save'):
		form = ClinicDateForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			messages.success(request, "Add Successfully")
			return redirect('/appsample/clinicDates')

	else:
		form = ClinicDateForm(instance=model)

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/appsample/clinicDates')

	context = {'form':form, 'filter':filter, 'page':page, 'reveal':True if pk else False}
	return render(request, 'clinicDate.html', context)



@allowed_users(roles = ['Receptionist', 'Doctor'])
def patient(request, pk=None):
	model = Patient.objects.get(pk=pk) if pk else Patient()

	data = Patient.objects.all()
	filter = PatientFilter(request.GET, queryset = data)
	data = filter.qs

	data_paginator = Paginator(data, 100)	
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)


	
	if request.POST.get('save'):
		form = PatientForm(request.POST, instance=model)
		userform = UserCreationForm(request.POST)

		if form.is_valid() and userform.is_valid():
			messages.success(request, "Add Successfully")
			userobj = userform.save()
			patient_group = Group.objects.get(name='Patient') 
			patient_group.user_set.add(userobj)
			patient_group.save()
			obj = form.save(commit=False)
			obj.user = userobj
			form.save()
			return redirect('/appsample/patients')

	else:
		form = PatientForm(instance=model, initial={'loyalty':1})
		userform = UserCreationForm()

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/appsample/patients')

	context = {'form':form, 'page':page, 'filter':filter, 'userform':userform}
	return render(request, 'patient.html', context)


@allowed_users(roles = ['Manager'])
def clinicDateEmployee(request, pk=None):
	model = ClinicDateEmployee.objects.get(pk=pk) if pk else ClinicDateEmployee()
	data = ClinicDateEmployee.objects.all()
	filter = ClinicDateEmployeeFilter(request.GET, queryset = data)
	data = filter.qs
	
	if request.POST.get('save'):
		form = ClinicDateEmployeeForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/clinicDateEmployee')

	else:
		form = ClinicDateEmployeeForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/clinicDateEmployee')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'clinicDateEmployee.html', context)


@allowed_users(roles = ['Manager'])
def designation(request, pk=None):
	model = Designation.objects.get(pk=pk) if pk else Designation()
	data = Designation.objects.all()
	filter = DesignationFilter(request.GET, queryset = data)
	data = filter.qs
	
	if request.POST.get('save'):
		form = DesignationForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/designations')

	else:
		form = DesignationForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/designations')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'designation.html', context)



@allowed_users(roles = ['Manager', 'Doctor'])
def diagnosis(request, pk=None):
	model = Diagnosis.objects.get(pk=pk) if pk else Diagnosis()
	data = Diagnosis.objects.all()
	filter = DiagnosisFilter(request.GET, queryset = data)
	data = filter.qs

	DiagnosisSymptomFormSet = inlineformset_factory(Diagnosis, DiagnosisSymptom, fields='__all__', extra=0 if pk else 1)

	# , widgets={'probability': TextInput(attrs = {'class':'form-control', 'placeholder':'Insert the Diagnosis' })}

	if request.POST.get('save'):
		form = DiagnosisForm(request.POST, instance=model)
		formset = DiagnosisSymptomFormSet(request.POST, instance=model)

		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
			return redirect('/appsample/diagnosises')

	else:
		form = DiagnosisForm(instance=model)
		formset = DiagnosisSymptomFormSet(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/diagnosises')

	context = {'form':form, 'data':data, 'filter':filter, 'formset':formset}
	return render(request, 'diagnosis.html', context)




def diagnosissymtom(request, pk=None):
	model = DiagnosisSymptom.objects.get(pk=pk) if pk else DiagnosisSymptom()
	data = DiagnosisSymptom.objects.all()
	filter = DiagnosisSymptomFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = DiagnosisSymptomForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/diagnosissymtoms')

	else:
		form = DiagnosisSymptomForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/diagnosissymtoms')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'diagnosissymtom.html', context)


@allowed_users(roles = ['Manager', 'Doctor', 'Nurse'])
def symptom(request, pk=None):
	model = Symptom.objects.get(pk=pk) if pk else Symptom()
	data = Symptom.objects.all()
	filter = SymptomFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = SymptomForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/symptoms')

	else:
		form = SymptomForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/symptoms')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'symptom.html', context)


def appointment(request, pk=None):
	model = Appointment.objects.get(pk=pk) if pk else Appointment()
	data = Appointment.objects.all()

	PrescriptionFormSet = inlineformset_factory(Appointment, Prescription, fields='__all__', extra=0 if pk else 1)

	filter = AppointmentFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = AppointmentForm(request.POST, instance=model)
		formset = PrescriptionFormSet(request.POST, instance=model)

		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
			return redirect('/appsample/appointments')

	else:
		form = AppointmentForm(instance=model)
		formset = PrescriptionFormSet(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/appointments')

	context = {'form':form, 'data':data, 'filter':filter, 'formset':formset}
	return render(request, 'appointment.html', context)

@allowed_users(roles = ['Manager', 'Receptionist'])
def appointment1(request, pk=None):
	model = Appointment.objects.get(pk=pk) if pk else Appointment()
	submodel = model.invoice if pk else Invoice()
	data = Appointment.objects.all()

	filter = AppointmentFilter1(request.GET, queryset = data)
	data = filter.qs

	data_paginator = Paginator(data, 100)	
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)

	
	if request.POST.get('save'):
		print(request.POST)
		form = AppointmentForm1(request.POST, instance=model)
		invoiceform = InvoiceForm2(request.POST)

		if form.is_valid() and invoiceform.is_valid():
			messages.success(request, "Add Successfully")
			obj = form.save(commit=False)
			form.save()
			invoiceobj = invoiceform.save(commit=False)
			invoiceobj.appointment = obj
			last_ref_no = Invoice.objects.last().reference_no
			invoiceobj.reference_no = 'BM' + str(int(last_ref_no[-3:]) + 1).zfill(3) ;
			invoiceobj.doctor_fee = obj.doctor.fee;
			invoiceform.save()			
			

			# increase occupide number
			clinicdate = ClinicDate.objects.get(id=request.POST['clinic_date'])
			clinicdate.occupied += 1
			clinicdate.save()

			# update loyalty
			num_appoit = obj.patient.appointment_set.count()
			try:
				loyalty = Loyalty.objects.get(minimum_appointment=num_appoit)
			except Loyalty.DoesNotExist:
				loyalty = None
			if loyalty:
				obj.patient.loyalty = loyalty
				obj.patient.save()
			return redirect('/appsample/appointments1')

	else:
		form = AppointmentForm1(instance=model)
		invoiceform = InvoiceForm2(instance= submodel)

		if request.POST:
			clinicdate = ClinicDate.objects.get(id=request.POST['clinic_date'])
			clinicdate.occupied -= 1
			clinicdate.save()
			#model.appoinment_status.id = 6
			model.save()
			messages.warning(request, "Delete Successfully")
			return redirect('/appsample/appointments1')

	context = {'form':form, 'filter':filter, 'page':page, 'invoiceform':invoiceform, 'reveal':True if pk else False}

	return render(request, 'appoinment1.html', context)

@allowed_users(roles = [ 'Doctor'])
def appointment2(request, pk=None):
	model = Appointment.objects.get(pk=pk) if pk else Appointment()
	data = Appointment.objects.all()

	# print(request.user.get_user_permissions())
	if request.user.has_perm('appsample.view_doctor'):
		data= Appointment.objects.filter(doctor__user=request.user).filter(clinic_date__start_time__date = datetime.today())

	filter = AppointmentFilter(request.GET, queryset = data)
	data = filter.qs

	data_paginator = Paginator(data, 100)	
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)

	
	if request.POST.get('save'):
		form = AppointmentForm2(request.POST, instance=model)

		if form.is_valid():
			messages.success(request, "Add Successfully")
			form.save()
			return redirect('/appsample/appointment2')

	else:
		form = AppointmentForm2(instance=model)

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/appsample/appointment2')

	context = {'form':form, 'page':page, 'filter':filter, 'reveal':True if pk else False}
	return render(request, 'appointment2.html', context)


def load_clinic_date(request):
    clinic_id = request.GET.get('clinic_id')
    clinic_dates = ClinicDate.objects.filter(clinic_id=clinic_id).all()
    return JsonResponse(list(clinic_dates.values('id', 'start_time', 'doctor')), safe=False)

def load_designation_employees(request):
    designation_id = request.GET.get('designation_id')
    designation_employees = Employee.objects.filter( designation_id= designation_id).all()
    return JsonResponse(list(designation_employees.values('user__id','user__username')), safe=False)

# def load_clinicdetails(request, pk):
#     clinic = Clinic.objects.get(pk=pk)
#     id = clinic.id
#     name = clinic.name
#     designation = clinic.designation.id
#     room = clinic.room.id
#     return JsonResponse({'id':id, 'name':name, 'designation':designation, 'room':room }, safe=False)

def load_doctor_clinic_date(request):
    doctor_id = request.GET.get('doctor_id')
    clinic_dates = ClinicDate.objects.filter(doctor_id=doctor_id).all()
    return JsonResponse(list(clinic_dates.values('id', 'start_time')), safe=False)

def load_symtoms(request):
    appointment_id = request.GET.get('appointment_id')
    appointmentsymtoms = Appointmentsymptom.objects.filter(appointment=appointment_id).all()
    return JsonResponse(list(appointmentsymtoms.values('id', 'symptom_id__name')), safe=False)


def load_appoinment_numbers(request):
    clinic_date_id = request.GET.get('clinic_date_id')
    appointmetnumber = Appointment.objects.filter(clinic_date_id=clinic_date_id).all()
    return JsonResponse(list(appointmetnumber.values('id', 'appo_no')), safe=False)

def load_clinic_date_details(request, pk):
    clinic_date = ClinicDate.objects.get(pk=pk)
    id = clinic_date.id
    clinic_id = clinic_date.clinic.id
    start_time = clinic_date.start_time
    currentno = clinic_date.currentno
    capacity = clinic_date.capacity
    occupied = clinic_date.occupied
    return JsonResponse({'id':id, 'start_time':start_time, 'currentno':currentno, 'capacity':capacity, 'occupied':occupied, 'clinic_id':clinic_id}, safe=False)

# def load_invoice_details(request, pk):
# 	invoice = Invoice.objects.get(pk=pk)
# 	id =



def load_appointment_details(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    id = appointment.id
    clinic_date = appointment.clinic_date.date
    number = appointment.appo_no
    patient = appointment.patient.name
    # symptoms = json.dumps(appointment.symptoms)
    symptoms = appointment.symptoms.all()
    symptom_list = []
    for symptom in symptoms: 
    	symptom_list.append(symptom.name)
  
    return JsonResponse({'id':id, 'clinic_date':clinic_date, 'number':number, 'patient':patient, 'symptoms':symptom_list}, safe=False)

def load_diagnosis(request):
	diagnosis_list = [{'id':1, 'name':'dengue', 'probability':0.3}, {'id':2, 'name':'Skin Cancer', 'probability':0.5}, {'id':1, 'name':'covid 19', 'probability':0.2}]
	return JsonResponse(diagnosis_list, safe=False)

@allowed_users(roles = ['Doctor', 'Receptionist'])
def prescription(request, pk=None):
	model = Prescription.objects.get(pk=pk) if pk else Prescription()
	data = Prescription.objects.all()
	filter = PrescriptionFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = PrescriptionForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/prescriptions')

	else:
		form = PrescriptionForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/prescriptions')

	context = {'form':form, 'data':data, 'filter':filter, 'reveal':True if pk else False}
	return render(request, 'prescription.html', context)

def appointmentDiagnosis(request, pk=None):
	model = AppointmentDiagnosis.objects.get(pk=pk) if pk else AppointmentDiagnosis()
	data = AppointmentDiagnosis.objects.all()
	filter = AppointmentDiagnosisFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = AppointmentDiagnosisForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/appointmentDiagnosis')

	else:
		form = AppointmentDiagnosisForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/appointmentDiagnosis')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'AppointmentDiagnosis.html', context)

def appointmentSymptom(request, pk=None):
	model = AppointmentSymptom.objects.get(pk=pk) if pk else AppointmentSymptom()
	data = AppointmentSymptom.objects.all()
	filter = AppointmentSymptomFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = AppointmentSymptomForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/appointmentSymptoms')

	else:
		form = AppointmentSymptomForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/appointmentSymptoms')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'appointmentSymptom.html', context)

def room(request, pk=None):
	model = Room.objects.get(pk=pk) if pk else Room()
	data = Room.objects.all()
	filter = RoomFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = RoomForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/rooms')

	else:
		form = RoomForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/rooms')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'room.html', context)


@allowed_users(roles = ['Doctor', 'Receptionist', 'Cashier'])
def service(request, pk=None):
	model = Service.objects.get(pk=pk) if pk else Service()
	data = Service.objects.all()
	filter = ServiceFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = ServiceForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/services')

	else:
		form = ServiceForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/services')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'service.html', context)

@allowed_users(roles = ['Receptionist', 'Cashier'])
def invoice(request, pk=None):
	model = Invoice.objects.get(pk=pk) if pk else Invoice()
	#submodel = model.services.all() if pk else {}
	data = Invoice.objects.all()
	filter = InvoiceFilter(request.GET, queryset = data)
	data = filter.qs

	InvoiceServiceFormSet = inlineformset_factory(Invoice, InvoiceService, fields='__all__', extra=1 if pk else 1)

	if request.POST.get('save'):
		form = InvoiceForm(request.POST, instance=model)
		formset = InvoiceServiceFormSet(request.POST, instance=model)

		if form.is_valid() and formset.is_valid():			
			form.save()
			formset.save()
			return redirect('/appsample/invoices')
			
	else:
		form = InvoiceForm(instance=model)
		formset = InvoiceServiceFormSet(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/invoices')
	discount_rate = model.appointment.patient.loyalty.discount if pk else 0
	context = {'form':form, 'data':data, 'filter':filter, 'formset':formset, 'reveal':True if pk else False, 'discount_rate':discount_rate}
	return render(request, 'invoice.html', context)
@csrf_exempt
def total(request):
	if request.POST:
		print(request.POST)
		invoice_num = request.POST['invoice']
		discount = request.POST['discount']
		discounted_total = request.POST['discounted_total']
		invoice = Invoice.objects.get(appointment__id = invoice_num)
		invoice.discount =Decimal(discount)
		invoice.discounted_total = Decimal(discounted_total)
		invoice.save()
	else:
		invoice_num = request.GET['invoice']
		invoice = Invoice.objects.get(appointment__id = invoice_num)
		total = invoice.appointment_fee + invoice.doctor_fee
		invoice_services = InvoiceService.objects.filter(invoice=invoice)
		for invoice_service in invoice_services:
			service_fee = invoice_service.service.charge
			multiple = invoice_service.multiple
			total += service_fee * multiple
		return JsonResponse({'total':total})

def payment(request, pk=None):
	model = Payment.objects.get(pk=pk) if pk else Payment()
	data = Payment.objects.all()
	filter = PaymentFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = PaymentForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/payments')

	else:
		form = PaymentForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/payments')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'payment.html', context)

def invoiceservice(request, pk=None):
	model = InvoiceService.objects.get(pk=pk) if pk else InvoiceService()
	data = InvoiceService.objects.all()
	filter = InvoiceServiceFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = InvoiceServiceForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/invoiceservices')

	else:
		form = InvoiceServiceForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/invoiceservices')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'invoiceservice.html', context)

def appoinmentstatus(request, pk=None):
	model = AppoinmentStatus.objects.get(pk=pk) if pk else AppoinmentStatus()
	data = AppoinmentStatus.objects.all()
	filter = AppoinmentStatusFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = AppoinmentStatusForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/appoinmentstatus')

	else:
		form = AppoinmentStatusForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/appoinmentstatus')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'appoinmentstatus.html', context)

def medicine(request, pk=None):
	model = Medicine.objects.get(pk=pk) if pk else Medicine()
	data = Medicine.objects.all()
	filter = MedicineFilter(request.GET, queryset = data)
	data = filter.qs

	
	if request.POST.get('save'):
		form = MedicineForm(request.POST, instance=model)

		if form.is_valid():
			form.save()
			return redirect('/appsample/medicines')

	else:
		form = MedicineForm(instance=model)

		if request.POST:
			model.delete()
			return redirect('/appsample/medicines')

	context = {'form':form, 'data':data, 'filter':filter}
	return render(request, 'medicine.html', context)

#Authentication

def test1 (request):
	if request.user.is_authenticated:
		return HttpResponse ('This is test 1')
	return HttpResponse ('Please login') 

#Authentication and authorization role base

def test2 (request):
	if request.user.is_authenticated:
		if request.user.groups.filter(name='Doctor').exists():
			return HttpResponse ('This is test 2')
		return HttpResponse ('your are not a doctor')

	return HttpResponse ('Please login') 

#Authentication and authorization permission base

def test3 (request):
	if request.user.is_authenticated:
		if request.user.has_perm('appsample.add_doctor'):
			return HttpResponse ('You can add club')
		return HttpResponse ('You cannot add club')
	return HttpResponse('Please Login')



def my_decarator(f):
	def f2(request):
		if request.user.is_authenticated:
			f(request)
		return HttpResponse('Hello')
	return f2


@my_decarator
def test4(request):
	return HttpResponse('This is test4') 


def userdetails (request):
    user = User.objects.all()   
    
    context={'user':user}
    return render(request, 'usersinfo.html', context)


# def tournament(request, pk=None):
#     model = Tournament.objects.get(pk=pk) if pk else Tournament()
#     data = Tournament.objects.all()

#     filter = TournamentFilter(request.GET, queryset = data)
#     data= filter.qs
    
#     data_paginator = Paginator(data, 5)
    
#     page_num = request.GET.get('page')
    
#     page = data_paginator.get_page(page_num)
    
#     if request.POST.get('save'):
#         form = TournamentForm(request.POST, instance=model)
        
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.created_by = request.user.username
#             obj.save()
#             form.save()
#             messages.success(request,"Successfully Add!!!")

#             news = News(title = request.POST.get('name'), description = request.POST.get('sport'), created_by = 'request.user.username')
#             news.save()

#             return redirect('/sample/tournament')
#     else:
#         form = TournamentForm(instance=model)
        
#         if request.POST:
#             model.delete()
#             messages.warning(request,"Are Sure Want to delete?")
#             return redirect('/sample/tournament')
            
#     context = {'form':form, 'filter':filter, 'page':page}
#     return render(request, 'tournament.html', context)


# def designation (request):
# 	form = DesignationForm()
# 	designations = Designation.objects.all() 
# 	filter = DesignationFilter(request.GET, queryset = designations)
# 	designations = filter.qs

	
# 	if request.method == 'POST':
# 		form = DesignationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('designation')
	
# 	context = {'designations':designations, 'form':form, 'filter':filter}
# 	return render(request, 'designation.html', context)	

# def updatedesignation (request, pk):
# 	designation = Designation.objects.get(id = pk)
# 	form = DesignationForm(instance = designation)

# 	if request.method == 'POST':
# 		form = DesignationForm(request.POST, instance = designation)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('designation')

# 	context = {'form':form}
# 	return render(request, 'designation.html', context)	

# def deletedesignation (request, pk):
# 	designation = Designation.objects.get(id = pk)
# 	if request.method == 'POST':
# 		designation.delete()
# 		return redirect ('designation')
		
# 	context = {'designation':designation}
# 	return render(request, 'deletedesignation.html', context)