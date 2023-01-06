from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrarPersona),
    path('creacionPersona/', views.creacionPersona),
    path('crearPersona/', views.crearPersona),
    path('actualizacionPersona/<identificacion>', views.actualizacionPersona),
    path('actualizarPersona/', views.actualizarPersona),
    path('eliminarPersona/<identificacion>', views.eliminarPersona),
]