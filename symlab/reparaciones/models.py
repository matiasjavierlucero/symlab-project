from django.db import models
from vehiculos.models import Vehiculo
# Create your models here.


class Reparacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.vehiculo)

    class Meta:
        verbose_name = 'Reparacion'
        verbose_name_plural = 'Reparaciones'
