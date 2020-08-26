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
# sekolah
	url(r'^$',views.index),
    url(r'^sekolah$',views.sekolah),
    url(r'^sekolah_insert$',views.sekolah_insert),
    url(r'^sekolah_delete/(?P<id>\d+)$', views.sekolah_delete, name='sekolah_delete'),
    url(r'^sekolah_edit/(?P<id>\d+)$', views.sekolah_delete, name='sekolah_edit'),
# siswwa
    url(r'^siswa$',views.siswa),
    url(r'^siswa_insert$',views.siswa_insert),
    url(r'^siswa_delete/(?P<id>\d+)$', views.siswa_delete, name='siswa_delete'),
    url(r'^siswa_edit/(?P<id>\d+)$', views.siswa_edit, name='sekolah_edit'),
    url(r'^siswa_proses/(?P<user>\w+)$', views.siswa_proses, name='siswa_proses'),

]
