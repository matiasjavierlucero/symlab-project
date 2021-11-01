
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Cliente


@pytest.mark.django_db
def test_cliente_view():
    cliente = Cliente.objects.create(
        apellido='Lucero',
        nombre='Matias Javier',
        dni=33524933,
        telefono=543584319481,
    )

    url = reverse("clientes:clientes-list")
    client = APIClient()

    response = client.get(url)
    print(response)
    assert response.json() == [
        dict(
            id=client.id,
            apellido='Lucero',
            nombre='Matias Javier',
            dni=33524933,
            telefono='15-4456-5678',
            created=client.created.isoformat(),
            updated=client.updated.isoformat(),
        )
    ]
