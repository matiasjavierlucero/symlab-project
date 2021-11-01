from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from .serializers import VehiculoSerializer
from .models import Vehiculo
from clientes.models import Cliente


class VehiculoViewSet(ViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request):
        serializer = VehiculoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        vehiculo = Vehiculo.objects.get(pk=pk)
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)

    def delete(self, request):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        return Response(serializer.errors)
