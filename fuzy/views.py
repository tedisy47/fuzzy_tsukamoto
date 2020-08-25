from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Sekolahform, Siswaform
from .models import Sekolah, Siswa

import requests
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
		'datasiswa' : Sekolah,

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
				'form' : Siswaform(),
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