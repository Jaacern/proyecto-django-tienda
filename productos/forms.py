# Django Imports
from django import forms
from django.forms.widgets import HiddenInput

# Project Imports


class AgregarAlPedido(forms.Form):
    # Formulario para la ventana modal que se abre 
    # al agregar un elemento al carrito de compras.
    cantidad_a_comprar = forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'ej: 1 (servicio) '
            }
        )
    )
    id_producto = forms.IntegerField(
        widget=forms.HiddenInput(
            attrs= {
                'class':'form-control',
                'value':'0',
                }
            )
        )
    
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_prd', 'descripcion', 'precio', 'id_categoria', 'imagen_prd', 'costo']
