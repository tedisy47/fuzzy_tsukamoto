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
from django.conf.urls import url ,include
from django.contrib.auth.urls import path

from . import views

urlpatterns = [

    url('admin/', admin.site.urls),
    url(r'^$',views.index, name='index'),
    url(r'^register/',views.index, name='index'),
    url(r'^login/',views.login, name='login'),
    url(r'^fuzzy/',include('fuzy.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

]
