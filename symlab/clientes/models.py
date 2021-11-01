from django.db import models


class Cliente(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido']
