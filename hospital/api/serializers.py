from rest_framework import serializers
from appsample.models import *


class ClinicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clinic 
		fields = '__all__'

# class EmployeeSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Employee 
# 		fields = '__all__'

class ClinicDateSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClinicDate 
		# fields = '__all__'
		exclude = ['nurse', 'doctor']
