from django.conf.urls import url
from django.urls import path

from . import views

urlpattern = [
	url(r'^$', views.HttpResponse, name='index'),
]