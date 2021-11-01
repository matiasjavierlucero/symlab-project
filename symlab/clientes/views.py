from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from .serializers import ClienteSerializer
from .models import Cliente


class ClienteViewSet(ViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def list(self, request, *args, **kwargs):
        clientes = ClienteSerializer(Cliente.objects.all(), many=True)
        return Response(clientes.data)

    def retrieve(self, request, pk=None):
        cliente = ClienteSerializer(Cliente.objects.get(pk=pk))
        return Response(cliente.data)

    def create(self, request, *args, **kwargs):
        cliente = ClienteSerializer(data=request.data)
        if cliente.is_valid():
            cliente.save()
            return Response(cliente.data)
        return Response(cliente.errors)
