from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from clientes import views

app_name = 'clientes'
schema_view = get_schema_view(title='Clientes', urlconf='clientes.urls')

router = routers.DefaultRouter()

router.register(r'clientes', views.ClienteViewSet, basename='clientes')

urlpatterns = [
    url(r'^', include(router.urls)),
]
