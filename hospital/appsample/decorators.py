from django.http import HttpResponse
from django.shortcuts import render, redirect


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		
		if request.user.is_authenticated:
			return redirect('patientaccount')
			
		else: 
			return view_func(request, *args, **kwargs)
	return wrapper_func

def unauthenticated_user2(view_func):
	def wrapper_func(request, *args, **kwargs):
		
		if request.user.is_authenticated:
			return redirect('dashboard')
			
		else: 
			return view_func(request, *args, **kwargs)
	return wrapper_func


def allowed_users(roles = []): 
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if request.user.is_superuser or request.user.groups.filter(name__in =roles).exists():
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('you are not authorized')
		return wrapper_func
	return decorator



def permission(permission):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if request.user.has_perm('appsample.add_clinic'):
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse ('You dont have permission')
		return wrapper_func
	return decorator



# decorator ekk output wenwanm eka decorator ekk . input eka mokk unath kamk na






















	# def unauthenticated_user(view_func):
	# def wrapper_func(request, *args, **kwargs):
		
	# 	if request.user.is_authenticated:
	# 		if request.user.groups=='Patient':
	# 			return redirect('dashboard')
	# 		elif request.user.groups=='Doctor':
	# 			return redirect('/appsample/employees')
			
	# 	else: 
	# 		return view_func(request, *args, **kwargs)
	# return wrapper_func