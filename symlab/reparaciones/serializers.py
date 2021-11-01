from rest_framework import serializers

from vehiculos.models import Vehiculo
from .models import Reparacion


class ReparacionSerializer(serializers.Serializer):
    vehiculo = serializers.PrimaryKeyRelatedField(
        queryset=Vehiculo.objects.all())
    fecha = serializers.DateField(format="%Y-%m-%d")
    descripcion = serializers.CharField(max_length=200)
    costo = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Reparacion
        fields = '__all__'

    def create(self, validated_data):
        return Reparacion.objects.create(**validated_data)

    def update(self, validated_data):
        instance = self.instance
        instance.vehiculo = validated_data.get('vehiculo', instance.vehiculo)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.descripcion = validated_data.get(
            'descripcion', instance.descripcion)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.costo = validated_data.get('costo', instance.costo)
        instance.save()
        return instance

    def list(self, validated_data):
        return Reparacion.objects.all().order_by('-fecha')

    def retrieve(self, validated_data):
        return Reparacion.objects.get(pk=validated_data.get('id'))

    def delete(self, instance):
        instance.delete()
        return instance
