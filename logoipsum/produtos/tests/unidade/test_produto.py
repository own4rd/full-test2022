from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from produtos.models.produto import Produto
from parameterized import parameterized


class ProdutoTestCase(APITestCase):
    @parameterized.expand([(1, 0.01), (8, 0.08)])
    def test_calculate_comissao(self, percentual, resultado):
        produto = Produto(percentual_comissao=percentual)
        self.assertEquals(resultado, produto.get_percentual_comissao())
