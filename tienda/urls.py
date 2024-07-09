# Django Imports
from django.urls import path

# App Imports
from . import views
from django.urls import path
from .views import AgregarProductoCarritoView, VerCarritoView, ActualizarCantidadProductoView, ProcesarCompraView


urlpatterns = [
    path('',views.tienda, name="Tienda"),
    path('<int:param_int>/<str:param_str>', views.tienda),
    path('agregar/<int:producto_id>/', AgregarProductoCarritoView.as_view(), name='agregar_al_carrito'),
    path('ver-carrito/', VerCarritoView.as_view(), name='ver_carrito'),
    path('actualizar/<int:producto_id>/', ActualizarCantidadProductoView.as_view(), name='actualizar_cantidad'),
    path('procesar-compra/', ProcesarCompraView.as_view(), name='procesar_compra'),
    

    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/nueva/', views.nueva_venta, name='nueva_venta'),
    path('ventas/modificar/<int:id>/', views.modificar_venta, name='modificar_venta'),
    path('ventas/eliminar/<int:id>/', views.eliminar_venta, name='eliminar_venta'),
]


