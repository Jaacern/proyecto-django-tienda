from django.db import models
from django.contrib.auth.models import User

class DatosAdicionales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30, verbose_name='Teléfono')
    rut = models.CharField(max_length=20, verbose_name='RUT',unique=True ,default='00000000000')

    def __str__(self):
        return f'Datos adicionales de {self.user.username}'

