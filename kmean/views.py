# from django.shortcuts import render
from django.shortcuts import  render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# import requests
import json

# Create your views here.
def index(request):
	return render(request,'login.html')
def login(request):
	if request.method == 'POST':
		# print(requests)
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active is True:
				auth_login(request, user)
				messages.add_message(request, messages.INFO, 'Selamat datang.')
				return redirect('/home/')
				# return HttpResponse('ok')
			else:
				return HttpResponse('gagal')
		else:
			return HttpResponse('gagal')
	else:
		return redirect('/fuzzy/')
def register(request):
	return render(request,'register.html')