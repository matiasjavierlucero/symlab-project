from django.db import models
from clientes.models import Cliente
# Create your models here.


class Vehiculo(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
