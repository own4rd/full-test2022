from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from clientes.models.cliente import Cliente


class ClienteTestCase(APITestCase):
    def setUp(self) -> None:
        self.url_client_list = reverse("cliente-list")
        self.cliente = Cliente.objects.create(nome="Cliente Um")
        return super().setUp()

    def test_user_create_successful(self):
        data = {"nome": "novo_cliente"}
        response = self.client.post(self.url_client_list, data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_user_detail_successful(self):
        detail_url = reverse("cliente-detail", kwargs={"pk": self.cliente.id})
        response = self.client.get(detail_url, format="json")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
