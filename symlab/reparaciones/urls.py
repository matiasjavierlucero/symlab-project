from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from reparaciones import views

app_name = 'reparaciones'
schema_view = get_schema_view(
    title='reparaciones', urlconf='reparaciones.urls')

router = routers.DefaultRouter()

router.register(r'reparaciones', views.ReparacionesViewSet,
                basename='reparaciones')

urlpatterns = [
    url(r'^', include(router.urls)),
]
