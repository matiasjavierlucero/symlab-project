from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import ReparacionSerializer
from .models import Reparacion
# Create your views here.


class ReparacionesViewSet(ViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Reparacion.objects.all().order_by('-fecha')
    serializer_class = ReparacionSerializer

    def list(self, request, *args, **kwargs):
        serializer = ReparacionSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Reparacion.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ReparacionSerializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReparacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Reparacion.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=204)
