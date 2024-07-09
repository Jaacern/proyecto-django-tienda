# Django Imports
from django.urls import path
from .views import salir

# App Imports
from . import views


urlpatterns = [
    path('',views.inicio, name="Inicio"),
     path('salir/',salir,name='salir'),
]