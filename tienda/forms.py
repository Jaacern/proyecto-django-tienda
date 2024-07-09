# Django Imports
from django import forms
from django.core.validators import MinValueValidator

#App Imports
from productos.models import Producto

class RealizarPedido(forms.Form):
    # crea el formulario para realizar el pedido
    producto = forms.ModelChoiceField(
        queryset= Producto.objects.all(),
        widget=forms.Select(
            attrs = {
                'class':'form-control',
                'placeholder': 'Producto',
            }
        )
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {
                'class':'form-control',
                'placeholder': 'ej: 1 servicio',
            }
        ),
        # Validador, el valor minimo que deja cargar es 1.
        validators=[MinValueValidator(1, message= "rambo")]
    )

class DatosInvitado(forms.Form):
    # Formulario que le pide los datos
    #  a los usuarios invitados
    nombre = forms.CharField()
    apellido = forms.CharField()
    teléfono = forms.CharField()

from django import forms

class AgregarProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, initial=1)

from django import forms
from django.core.validators import MinValueValidator
from .models import Producto

class RealizarPedidoForm(forms.Form):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Producto',
            }
        )
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad (ej: 1 servicio)',
            }
        ),
        validators=[MinValueValidator(1, message="La cantidad mínima debe ser 1.")]
    )

class ModificarVentaForm(forms.Form):
    # Formulario para modificar una venta
    id_venta = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ID de la venta a modificar',
            }
        )
    )
    # Otros campos que puedas necesitar para modificar la venta

class DatosInvitadoForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }
        )
    )
    apellido = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
            }
        )
    )
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
            }
        )
    )

    # Otros formularios que puedas necesitar para tu aplicación


# tienda/forms.py
from django import forms
from .models import Venta

# tienda/forms.py
from django import forms
from .models import Venta, Detalle_Venta

class RealizarPedidoForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id_usuario', 'nombre_inv', 'apellido_inv', 'telefono_inv'] # Ajusta los campos según los que tengas en tu modelo Venta

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = Detalle_Venta
        fields = ['id_producto', 'cant_vendida', 'precio_unitario']  # Ajusta los campos según los que tengas en tu modelo Detalle_Venta



