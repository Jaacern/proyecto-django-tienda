# Django Imports
from django.urls import path
from .views import lista_productos, crear_producto, editar_producto, eliminar_producto

# App Imports
from . import views


urlpatterns = [
    path('',views.productos, name="Productos"),
    path('<int:param>/', views.productos),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('editar/<int:id>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
]
