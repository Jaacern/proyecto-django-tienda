# Django Imports
from django.urls import path

# App Imports
from . import views


urlpatterns = [
    path('',views.register, name='Register'),     
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
from django.urls import path
from . import views

