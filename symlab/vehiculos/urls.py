from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from vehiculos import views

app_name = 'vehiculos'
schema_view = get_schema_view(title='Vehiculos', urlconf='vehiculos.urls')

router = routers.DefaultRouter()

router.register(r'vehiculos', views.VehiculoViewSet, basename='vehiculos')

urlpatterns = [
    url(r'^', include(router.urls)),
]
