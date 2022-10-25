from django.urls import reverse
from django.test import TestCase
from clientes.models.cliente import Cliente
from vendas.models.vendedor import Vendedor
from produtos.models.item import Item 
from produtos.models.produto import Produto 
from produtos.models.servico import Servico 
from vendas.models.venda import Venda, ItemVenda
from parameterized import parameterized
import datetime
from rest_framework import status
from rest_framework.test import APITestCase


class VendaTestCase(TestCase):
    @parameterized.expand([(8, 3), (5, 3), (4, 2.4)])
    def test_get_comissao_item_madrugada_manha(self, comissao, total_comissao):
        # Ano,Mês,Dia: Hora, Minuto, Segundos 
        venda = Venda(data=datetime.datetime(2022,5,7, 9, 0, 0))
        item = Item(percentual_comissao=comissao)
        itemvenda = ItemVenda(venda=venda, quantidade=2, preco_item_unidade=30, item=item)
        self.assertEquals(itemvenda.get_comissao_item(), total_comissao)


    @parameterized.expand([(8, 4.8), (5, 3), (4, 2.4), (1, 2.4)])
    def test_get_comissao_item_tarde_noite(self, comissao, total_comissao):
        # Ano,Mês,Dia: Hora, Minuto, Segundos 
        venda = Venda(data=datetime.datetime(2022,5,7, 13, 0, 0))
        item = Item(percentual_comissao=comissao)
        itemvenda = ItemVenda(venda=venda, quantidade=2, preco_item_unidade=30, item=item)
        self.assertEquals(itemvenda.get_comissao_item(), total_comissao)

    @parameterized.expand([(10, 33.80, 338), (20, 34.90, 698)])
    def test_preco_total_item(self, quantidade, preco_item_unidade, total):
        itemvenda = ItemVenda(
            quantidade=quantidade, preco_item_unidade=preco_item_unidade
        )
        self.assertEquals(itemvenda.get_preco_total_item(), total)

    @parameterized.expand([(4, 0.04), (5, 0.05), (6, 0.05)])
    def test_calculo_comissao_madrugada_manha(
        self, item_percentual_comissao, resultado_ercentual_comissao
    ):
        itemvenda = ItemVenda(item=Item(percentual_comissao=item_percentual_comissao))
        self.assertEquals(
            itemvenda.get_calculo_comissao_madrugada_manha(),
            resultado_ercentual_comissao,
        )

    @parameterized.expand([(4, 0.04), (5, 0.05), (6, 0.06), (1, 0.04)])
    def test_calculo_comissao_madrugada_manha(
        self, item_percentual_comissao, resultado_ercentual_comissao
    ):
        itemvenda = ItemVenda(item=Item(percentual_comissao=item_percentual_comissao))
        self.assertEquals(
            itemvenda.get_calculo_comissao_tarde_noite(), resultado_ercentual_comissao
        )

    @parameterized.expand([(12, 0, 0, True), (12, 0, 1, False), (23, 59, 59, False)])
    def test_is_venda_efetuada_madrugada_manha(self, hora, minuto, segundo, result_is_manha):
        # Ano,Mês,Dia: Hora, Minuto, Segundos 
        venda = Venda(data=datetime.datetime(2022,5,7,hora,minuto,segundo))
        self.assertEquals(venda.is_venda_efetuada_madrugada_manha(), result_is_manha)



class VendaApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.vendedor = Vendedor.objects.create(nome='Vendedor')
        self.cliente = Cliente.objects.create(nome='Cliente')
        self.produto = Produto.objects.create(nome="Produto 1", preco=20, percentual_comissao=8)
        self.servico = Servico.objects.create(nome="Serviço 1", preco=50, percentual_comissao=4)
 
        return super().setUp()

    def test_calcular_total_produto(self):
        data = {
            "vendedor": self.vendedor.pk,
            "cliente": self.cliente.pk,
            "itensvenda": [
                {'quantidade': 20, 'item': self.produto.pk},
                {'quantidade': 30, 'item': self.servico.pk},
            ]
        }
        detail_url = reverse("venda-list")
        response = self.client.post(detail_url, data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Venda.objects.first().itens.count(), 2)
        self.assertEquals(Venda.objects.first().calcular_total_venda(), 1900)
                
    def test_calcular_total_comissao(self):
        """
        Periodo da tarde no mínimo 0.04%
        """
        venda = Venda.objects.create(vendedor=self.vendedor, cliente=self.cliente)
        venda.data = datetime.datetime(2022,1,1,13,0,0)
        venda.save()

        itemvenda_1 = ItemVenda(
            item=self.produto,
            preco_item_unidade=self.produto.preco,
            quantidade=10,
            venda=venda
        )
        itemvenda_1.save()
        itemvenda_2 = ItemVenda(
            item=self.servico,
            preco_item_unidade=self.servico.preco,
            quantidade=10,
            venda=venda
        )
        itemvenda_2.save()
        self.assertEquals(venda.calcular_total_comissao(), 36.00)