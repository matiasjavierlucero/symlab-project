from rest_framework import serializers
from .models import Vehiculo
from clientes.models import Cliente
from reparaciones.models import Reparacion
from reparaciones.serializers import ReparacionSerializer


class VehiculoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all())
    reparaciones = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Vehiculo
        fields = '__all__'

    def get_reparaciones(self, obj):
        return ReparacionSerializer(Reparacion.objects.filter(vehiculo_id=obj.id), many=True).data

    def create(self, validated_data):
        return Vehiculo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.placa = validated_data.get('placa', instance.placa)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.anio = validated_data.get('anio', instance.anio)
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

    def list(self, validated_data):
        return Vehiculo.objects.all()
