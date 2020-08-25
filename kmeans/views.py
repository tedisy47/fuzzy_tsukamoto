from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Datasetform
from .models import Dataset, Klaster, Proses

import requests
import math
# Create your views here.
def index(request):

	datasiswa = Dataset.objects.all()
	context	= {
		'page_title': 'Siswa',
		'title': 'Data Siswa',
		'datasiswa' : datasiswa,

	}
	return render(request,'page/dataset.html',context)
def dataset_edit(request,id):
	pass
def dataset_delete(request,id):
	Dataset.objects.filter(id=id).delete()
	return redirect('/kmean')
def dataset_insert(request):
	context = {
		'page_title': 'Siswa',
		'title': 'Tambah Data Siswa',
		'url': 'proses_insert',
		'form' : Datasetform(),
	}
	return render(request,'form.html',context)
def proses_insert_dataset(request):
	form = Datasetform(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/kmean/')
	return redirect('/kmean/')

def insert_klaster(request,index=1):
	kluster = Dataset.objects.all()[:3]
	check = Klaster.objects.filter(index=index)
	if not len(check):
		for kluster in kluster:
			data = Klaster(a=kluster.x, b=kluster.y, index=index)
			data.save()
	return redirect('/kmean/proses/'+str(index))

def proses(request, index=1):
	dataset = Dataset.objects.all()
	klaster = Klaster.objects.all()
	for dataset_list in dataset:
		kl =1
		for klaster_list in klaster:
			x = dataset_list.x - klaster_list.a
			x = x**2
			y = dataset_list.y - klaster_list.b
			y = y**2
			hasil = x + y
			hasil = math.sqrt(hasil)
			data = Proses(hasil=hasil, dataset_id=dataset_list.id, kluster=kl, index_kluster=index)
			data.save()
			kl = kl+1


	return HttpResponse(index)