from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import Sekolahform, Siswaform
from .models import Sekolah, Siswa, Proses

import urllib.parse

import requests
import json

import urllib.request
import math
import http.client


# Create your views here.

def index(request):
	sekolah = Sekolah.objects.all()
	context	= {
		'page_title': 'sekolah',
		'title': 'Data sekolah',
		'datasekolah' : sekolah,

	}
	return render(request,'page/sekolah.html',context)
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
def sekolah_edit(request,id):
	instance = get_object_or_404(Sekolah, id=id)
	print(instance)
	if request.method == 'POST':
		form = Sekolahform(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('/fuzzy/sekolah')
		else:
			context = {
				'page_title': 'sekolah',
				'title': 'Edit Data sekolah',
				'url': 'proses_insert',
				'form' : Sekolahform(instance=instance),
			}
			return render(request,'page/form_sekolah.html',context)
	else :
		context = {
			'page_title': 'sekolah',
			'title': 'Tambah Data sekolah',
			'url': 'proses_insert',
			'form' : Sekolahform(instance=instance),
		}
		return render(request,'page/form_sekolah.html',context)
def sekolah_delete(request,id):
	Sekolah.objects.filter(id=id).delete()
	return redirect('/fuzzy/sekolah')
def sekolah_detail(request,id):
	sekolah = Sekolah.objects.filter(id=id).all()
	context	= {
		'page_title': 'Sekolah',
		'title': 'Detail Sekolah',
		'datasekolah' : sekolah,

	}
	return render(request,'page/sekolah_detail.html',context)
def siswa(request):
	siswa = Siswa.objects.all()
	count = Siswa.objects.filter(user=request.user).count()
	print(request.user)
	print(count)
	context	= {
		'page_title': 'siswa',
		'title': 'Data Siswa',
		'count': count,
		'datasiswa' : siswa,

	}
	return render(request,'page/siswa.html',context)
def siswa_insert(request):
	if request.method == 'POST':
		form = Siswaform(request.POST)
		if form.is_valid():
			siswa = Siswa.objects.filter(user=request.user).all()
			if siswa is None:
				form.save()
				return redirect('/fuzzy/siswa')
			else :				
				
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
def siswa_edit(request,id):
	instance = get_object_or_404(Siswa, id=id)
	print(instance)
	if request.method == 'POST':
		form = Siswaform(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('/fuzzy/siswa')
		else:
			context = {
				'page_title': 'siswa',
				'title': 'Edit Data siswa',
				'url': 'proses_insert',
				'form' : Siswaform(instance=instance),
			}
			return render(request,'page/form_sekolah.html',context)
	else :
		context = {
			'page_title': 'siswa',
			'title': 'Tambah Data siswa',
			'url': 'proses_insert',
			'form' : Siswaform(instance=instance),
		}
		return render(request,'page/form_sekolah.html',context)
def siswa_delete(request,id):
	Siswa.objects.filter(id=id).delete()
	return redirect('/fuzzy/siswa')	

def siswa_proses(request,user):
	dell = Proses.objects.filter(user=user).delete()
	siswa = Siswa.objects.filter(user=user).values()
	sekolah = Sekolah.objects.values()

	da = []
	zz = ""
	for siswa_1 in siswa:
		link = ""
		for sekolah_1 in sekolah:
			loc_destination = sekolah_1.get('lat')
			loc_destination = loc_destination.split(',')
			lat_destination = loc_destination[0]
			lat_destination = lat_destination.replace('(','')
			long_destination = loc_destination[1]
			long_destination = long_destination.replace(')','')

			loc_origin = siswa_1.get('lat')
			loc_origin = loc_origin.split(',')
			lat_origin = loc_origin[0]
			lat_origin = lat_origin.replace('(','')
			long_origin = loc_origin[1]
			long_origin = long_origin.replace(')','')
			# link = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+lat_destination+","+long_destination+"&destinations="+lat_destination+","+long_destination+"&key=AIzaSyAgINDzGpgwWpcZtnOLuw5DtWcrO_VUsoE&mode=driving&language=id"
			

			url = "https://google.com/maps/api/distancematrix/json"

			querystring = {"unitsi":"mperialunits=imperial","origins": lat_origin+", "+long_origin,"destinations": lat_destination+","+long_destination,"key":"AIzaSyAgINDzGpgwWpcZtnOLuw5DtWcrO_VUsoE","mode":"driving","language":"id' (found at least ' ')"}

			headers = {
			    'cache-control': "no-cache",
			    'postman-token': "ea30c2d1-c81a-62fe-1cf8-6b7276faf7f5"
			    }

			response = requests.request("GET", url, headers=headers, params=querystring)

			res = json.loads(response.text)
			# print(res)
			value = ""
			for rows in res['rows']:
				val = ""
				for elements in rows.get('elements'):
					distance = elements.get('distance')
					vl = distance.get('value')
					val +=str(vl)
				value += str(val)
			value = int(value)
			jarak_dekat = (13000 - value)/(13000-200)
			jarak_jauh = (value - 200)/(13000-200)
			b = sekolah_1.get("biaya")

			biaya_murah = (2000000 - b)/(2000000-500000)
			biaya_mahal = (b - 500000)/(2000000-500000)
			# predikat 1
			predikat1 = [jarak_dekat,biaya_murah]
			# print(predikat1)
			min_predikat1 = min(predikat1)
			min_predikat1 = float(min_predikat1)
			# print(min_predikat1)

			# z1
			if min_predikat1 == predikat1[0]:
				z1 = 13000 -(min_predikat1* (13000-200))
			else:
				z1 = 2000000 -(min_predikat1* (2000000-500000))
			# print(z1)
			z1 = float(z1)
			# print(z1)
			# predikat 2

			predikat2 = [jarak_dekat,biaya_mahal]
			# print(predikat2)
			min_predikat2 = min(predikat2)
			# print(min_predikat2)

			# z2
			if min_predikat2 == predikat2[0]:
				z2 = 13000 -(min_predikat2* (13000-200))
			else:
				z2 = 2000000 -(min_predikat2* (2000000-500000))
			
			# predikat 3

			predikat3 = [jarak_jauh,biaya_murah]
			# print(predikat3)
			min_predikat3 = min(predikat3)
			# print(min_predikat3)

			# z3
			if min_predikat3 == predikat3[0]:
				z3 = 13000 -(min_predikat3* (13000-200))
			else:
				z3 = 2000000 -(min_predikat3* (2000000-500000))


			# predikat 3

			predikat4 = [jarak_jauh,biaya_mahal]
			# print(predikat4)
			min_predikat4 = min(predikat4)
			# print(min_predikat4)

			# z3
			if min_predikat4 == predikat4[0]:
				z4 = 13000 -(min_predikat4* (13000-200))
			else:
				z4 = 2000000 -(min_predikat4* (2000000-500000))
			
			zn1 = min_predikat1*z1
			zn2 = min_predikat2 * z2
			zn3 = min_predikat3 * z3
			zn4 = min_predikat4 * z4
			bobot_atas = zn1+zn2+zn3+zn4
			bobot_bawah = min_predikat1+min_predikat2+min_predikat3+min_predikat4
			bobot = bobot_atas/bobot_bawah

			# print(bobot)


			skl = Sekolah.objects.count()
			p = Proses.objects.filter(user=siswa_1.get("user")).count()
			print(p)
			if p < skl:
				proses =Proses(
					nama_sekolah = sekolah_1.get("nama_sekolah"),
					alamat_sekolah = sekolah_1.get("alamat_sekolah"),
					jarak = value,
					biaya = sekolah_1.get("biaya"),
					user = siswa_1.get("user"),
					bobot = bobot
					)
				proses.save();
				

	return redirect('/fuzzy/siswa_detail/'+user)

	# return HttpResponse('tes')	

def siswa_detail(request,user):
	siswa = Siswa.objects.filter(user=user).all()
	rekomendasi = Proses.objects.filter(user=user).order_by('+bobot').all()
	context	= {
		'page_title': 'siswa',
		'title': 'Biodata Siswa',
		'title2': 'Rekomendasi Sekolah',
		'datasiswa' : siswa,
		'rekomendasi' : rekomendasi,

	}
	return render(request,'page/siswa_detail.html',context)