from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from appsample.models import *
from .serializers import *


class ClinicView(viewsets.ModelViewSet):
	
	queryset = Clinic.objects.all()
	serializer_class = ClinicSerializer

# class ClinicByDesignation(generics.ListAPIView):

# 	serializer_class = ClinicSerializer

# 	def get_queryset(self):
# 		designation = self.kwargs['designation_id']
# 		return Clinic.objects.filter(designation_id=designation)


class ClinicDateView(viewsets.ModelViewSet):
	
	queryset = ClinicDate.objects.all()
	serializer_class = ClinicDateSerializer



# class EmployeeView(viewsets.ModelViewSet):
# 	queryset = Employee.objects.filter(designation_id = self.kwargs['designation_id'])
# 	serializer_class = EmployeeSerializer
	# filter_fields = ['designation_id']
	# filter_backends = (filters.DjangoFilterBackend,)