from django.shortcuts import render
from appsample.models import *
from appsample.views import *
from .forms import *


# Create your views here.
def home (request):
	clinics = Clinic.objects.all()
	clinicDates = ClinicDate.objects.all()
	
	context = {'clinics':clinics, 'clinicDates':clinicDates}
	return render(request, 'home.html', context)

def confirm (request):
	return render(request, 'confirm.html')

def calendar (request):
	data = Appointment.objects.all()
	return render(request, 'calendar.html')

def skincare (request):
	return render(request, 'skincare.html')

def eyecare (request):
	return render(request, 'eyecare.html')

def entcare (request):
	return render(request, 'entcare.html')

def makeAppointment (request):
	clinics = Clinic.objects.all()
	clinicDates = ClinicDate.objects.all()
	p_details = Patient.objects.filter(user=request.user.id).all()

	context = {'clinics':clinics, 'clinicDates':clinicDates, 'p_details':p_details}
	return render(request, 'makeappointment.html', context)

# def patientAccount (request):
# 	appointment = Appointment.objects.filter(patient=request.user.id).order_by('-clinic_date__start_time')
# 	clinics = Clinic.objects.all()
# 	clinicDates = ClinicDate.objects.all()
# 	p_details = Patient.objects.filter(user=request.user.id).all()
# 	symptoms = Symptom.objects.all()
# 	news = News.objects.all()

# 	context = {'appointment':appointment, 'clinics':clinics, 'clinicDates':clinicDates, 'p_details':p_details, 'symptoms':symptoms, 'news':news}
# 	return render(request, 'patientaccount.html', context)

def newsdetails (request, pk=None):
	already_read = request.user.news_set.all()
	model = News.objects.get(pk=pk) if pk else News()
	data = News.objects.all()
	data = data.difference(already_read)
	if request.POST.get('save'):
		form = NewsForm(request.POST, instance=model)
		if form.is_valid():
			#form.save()
			crby = News(created_by = request.user, title = request.POST.get('title'), description = request.POST.get('description') )
			crby.save()
			messages.success(request, "Add Successfully")
			return redirect('/website/newsdetails')

	else:
		form = NewsForm(instance=model)

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/website/newsdetails')

	context = {'form':form, 'data':data}
	return render(request, 'news.html', context)

def newsread (request, pk):  
    news = News.objects.get(id=pk)
    news.readers.add(request.user)
    
    return redirect(newsdetails)


def newsdetails2 (request, pk=None):
	already_read = request.user.news2_set.all()
	model = News2.objects.get(pk=pk) if pk else News2()
	data = News2.objects.all()
	data = data.difference(already_read)
	if request.POST.get('save'):
		form = NewsForm2(request.POST, instance=model)
		if form.is_valid():
			#form.save()
			crby = News2(created_by = request.user, title = request.POST.get('title'), description = request.POST.get('description') )
			crby.save()
			messages.success(request, "Add Successfully")
			return redirect('/website/newsdetails2')

	else:
		form = NewsForm2(instance=model)

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/website/newsdetails2')

	context = {'form':form, 'data':data}
	return render(request, 'news2.html', context)

def newsread2 (request, pk):  
    news = News2.objects.get(id=pk)
    news.readers.add(request.user)
    
    return redirect(newsdetails2)


def newsview (request):
	data = News.objects.all().order_by('-created_at')
	data2 = News2.objects.all().order_by('-created_at')

	context = { 'data':data, 'data2':data2}
	return render(request, 'newsview.html', context)


def patientAccount(request, pk=None):
	loyalty = Patient.objects.get(user=request.user).loyalty
	appointment = Appointment.objects.filter(patient=request.user.id).order_by('-clinic_date__start_time')
	p_details = Patient.objects.filter(user=request.user.id).all()
	news = News.objects.all()
	model = Appointment.objects.get(pk=pk) if pk else Appointment()
	submodel = model.invoice if pk else Invoice()
	data = Appointment.objects.all()
	

	data_paginator = Paginator(data, 100)	
	page_num = request.GET.get('page')
	page = data_paginator.get_page(page_num)

	
	if request.POST.get('save'):
		form = patientAccountForm(request.POST, instance=model)
		invoiceform = InvoiceForm2(request.POST)

		if form.is_valid() and invoiceform.is_valid():
			messages.success(request, "Added Successfully")
			obj = form.save(commit=False)
			obj.patient = Patient.objects.get(user=request.user)
			form.save()
			invoiceobj = invoiceform.save(commit=False)
			invoiceobj.appointment = obj
			last_ref_no = Invoice.objects.last().reference_no
			invoiceobj.reference_no = 'BM' + str(int(last_ref_no[-3:]) + 1).zfill(3) ;
			invoiceobj.doctor_fee = obj.doctor.fee;
			# invoiceobj.appointment_fee = 1000;
			invoiceform.save()			
			

			# increase occupide number
			clinicdate = ClinicDate.objects.get(id=request.POST['clinic_date'])
			clinicdate.occupied += 1
			clinicdate.save()
			
			# update loyalty
			num_appoit = obj.patient.appointment_set.count()
			if num_appoit > 4 :
				obj.patient.loyalty.id += 1
				obj.patient.save()

			return redirect('/website/patientaccount')

	else:
		form = patientAccountForm(instance=model)
		invoiceform = InvoiceForm2(instance= submodel)

		if request.POST:
			model.delete()
			messages.warning(request, "Delete Successfully")
			return redirect('/website/patientaccount')


	context = {'form':form, 'page':page, 'invoiceform':invoiceform, 'p_details':p_details, 'news':news, 'appointment':appointment, 'loyalty':loyalty}
	return render(request, 'patientaccount.html', context)