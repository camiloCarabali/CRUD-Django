from django.urls import re_path
from PersonApp import views

urlpatterns=[
    re_path(r'mostrarProfesion/$', views.mostrarProfesion),
    re_path(r'crearProfesion/$', views.crearProfesion),
    re_path(r'actualizarProfesion/$', views.actualizarProfesion),
    re_path(r'eliminarProfesion/([0-9]+)$', views.eliminarProfesion),
    re_path(r'mostrarPersona/$', views.mostrarPersona),
    re_path(r'crearPersona/$', views.crearPersona),
    re_path(r'actualizarPersona/$', views.actualizarPersona),
    re_path(r'eliminarPersona/([0-9]+)$', views.eliminarPersona),
]