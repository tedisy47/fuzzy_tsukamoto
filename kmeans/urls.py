"""kmean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include

from . import views

urlpatterns = [

	url(r'^$',views.index),
	url(r'^dataset_insert',views.dataset_insert),
	url(r'^proses_insert',views.proses_insert_dataset),
	url(r'^insert_klaster',views.insert_klaster),
    url(r'^proses/(?P<index>\d+)$', views.proses,),
    url(r'^dataset_delete/(?P<id>\d+)$', views.dataset_delete, name='dataset_delete'),
    url(r'^dataset_edit/(?P<id>\d+)$', views.dataset_delete, name='dataset_edit'),

]
