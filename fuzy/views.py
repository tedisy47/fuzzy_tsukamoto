from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Sekolahform, Siswaform
from .models import Sekolah, Siswa

import requests

import urllib.request
import math


# Create your views here.

def index(request):
	context	= {
		'page_title': 'sekolah',
		'title': 'Data sekolah',

	}
	return render(request,'page/dataset.html',context)
def sekolah(request):
	sekolah = Sekolah.objects.all()
	context	= {
		'page_title': 'sekolah',
		'title': 'Data sekolah',
		'datasekolah' : sekolah,

	}
	return render(request,'page/sekolah.html',context)
def sekolah_insert(request):
	if request.method == 'POST':
		form = Sekolahform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/fuzzy/sekolah')
		else:
			context = {
				'page_title': 'sekolah',
				'title': 'Tambah Data sekolah',
				'url': 'proses_insert',
				'form' : Sekolahform(),
			}
			return render(request,'page/form_sekolah.html',context)
	else :
		context = {
			'page_title': 'sekolah',
			'title': 'Tambah Data sekolah',
			'url': 'proses_insert',
			'form' : Sekolahform(),
		}
		return render(request,'page/form_sekolah.html',context)
def sekolah_edit():
	pass
def sekolah_delete(request,id):
	Sekolah.objects.filter(id=id).delete()
	return redirect('/fuzzy/sekolah')
def siswa(request):
	siswa = Siswa.objects.all()
	context	= {
		'page_title': 'siswa',
		'title': 'Data Siswa',
		'datasiswa' : siswa,

	}
	return render(request,'page/siswa.html',context)
def siswa_insert(request):
	if request.method == 'POST':
		form = Siswaform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/fuzzy/siswa')
		else:
			context = {
				'page_title': 'siswa',
				'title': 'Tambah Data Siswa',
				'url': 'proses_insert',
				'form' : form,
			}
			return render(request,'page/form_sekolah.html',context)
	else :
		context = {
			'page_title': 'siswa',
			'title': 'Tambah Data Siswa',
			'url': 'proses_insert',
			'form' : Siswaform(),
		}
		return render(request,'page/form_sekolah.html',context)
def siswa_edit():
	pass
def siswa_delete(request,id):
	Siswa.objects.filter(id=id).delete()
	return redirect('/fuzzy/siswa')	

def siswa_proses(request,user):
	siswa = Siswa.objects.filter(user=user).values()
	sekolah = Sekolah.objects.values()
	da = []
	for siswa_1 in siswa:
		for sekolah_1 in sekolah:
			loc_destination = sekolah_1.get('lat')
			loc_destination = loc_destination.split(',')
			lat_destination = loc_destination[0]
			lat_destination = lat_destination.replace('(','')
			long_destination = loc_destination[1]
			long_destination = long_destination.replace(')','')
			print(lat_destination)
			print(long_destination)
			# link = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+lat_destination+","+long_destination+"&destinations="+lat_destination+","+long_destination+"&key=AIzaSyAgINDzGpgwWpcZtnOLuw5DtWcrO_VUsoE&mode=driving&language=id"
			
			a = urllib.request.urlopen("http://google.com/maps/api/distancematrix/json?units")
			print(a)			
		

	return HttpResponse(a)