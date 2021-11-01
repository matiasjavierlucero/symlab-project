from rest_framework import serializers
from .models import Cliente
from vehiculos.models import Vehiculo
from vehiculos.serializers import VehiculoSerializer


class ClienteSerializer(serializers.Serializer):
    apellido = serializers.CharField()
    nombre = serializers.CharField()
    dni = serializers.CharField()
    telefono = serializers.CharField()
    vehiculos = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance

    def validate_dni(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "El DNI debe contener solo numeros")
        return value

    def validate_telefono(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "El telefono debe contener solo numeros")
        return value

    def validate_apellido(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "El apellido debe contener solo letras")
        return value

    def validate_nombre(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "El nombre debe contener solo letras")
        return value

    def get_vehiculos(self, obj):
        return VehiculoSerializer(Vehiculo.objects.filter(cliente_id=obj.id), many=True).data

    class Meta:
        model = Cliente
        fields = ('id', 'apellido', 'nombre', 'dni', 'telefono')
