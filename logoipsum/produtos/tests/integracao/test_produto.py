from django.urls import reverse
from parameterized import parameterized, param

from rest_framework import status
from rest_framework.test import APITestCase
from produtos.models.produto import Produto


class ProdutoTestCase(APITestCase):
    def setUp(self) -> None:
        self.data = {"nome": "Novo Produto", "preco": 20.0, "percentual_comissao": 4}
        self.url_client_list = reverse("produto-list")
        self.produto = Produto.objects.create(**self.data)
        return super().setUp()

    def test_produto_create_successful(self):
        response = self.client.post(self.url_client_list, self.data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_produto_detail_successful(self):
        detail_url = reverse("produto-detail", kwargs={"pk": self.produto.id})
        response = self.client.get(detail_url, format="json")
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    @parameterized.expand(
        [
            (
                {"nome": "Novo Produto", "preco": 20.0, "percentual_comissao": None},
                "percentual_comissao",
                "Este Campo Não Pode Ser Nulo.",
            ),
            (
                {"nome": "Novo Produto", "preco": None, "percentual_comissao": 9},
                "preco",
                "Este Campo Não Pode Ser Nulo.",
            ),
            (
                {"nome": "Novo Produto", "preco": 20.0, "percentual_comissao": 22},
                "percentual_comissao",
                "O Percentual De Comissão Deve Ser Entre 0 E 10.",
            ),
        ]
    )
    def test_produto_create_should_fail(self, data, field, message):
        """
        Data: Produtos a serem criados
        Field: Campo sendo testado
        Message: Mensagem de erro relacionada
        """
        response = self.client.post(self.url_client_list, data, format="json")
        error_message = response.data.get(field)[0].title()
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(message, error_message)
