from django.db import models

from produtos.models.item import Item
from vendas.models.vendedor import Vendedor
from clientes.models.cliente import Cliente


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    itens = models.ManyToManyField(Item, through="ItemVenda")

    COMISSAO1_START_AT = "00:00:00"
    COMISSAO1_END_AT = "12:00:00"

    def __str__(self) -> str:
        return f"{self.data} - {self.vendedor}"

    def calcular_total_venda(self):
        total_venda = 0
        for itemvenda in self.itensvenda.all():
            total_venda += itemvenda.get_preco_total_item()
        return total_venda

    def calcular_total_comissao(self):
        total_comissao = 0
        for itemvenda in self.itensvenda.all():
            total_comissao += itemvenda.comissao_vendedor
        return total_comissao

    def is_venda_efetuada_madrugada_manha(self):
        return (
            self.data.time().strftime("%H:%M:%S") >= self.COMISSAO1_START_AT
            and self.data.time().strftime("%H:%M:%S") <= self.COMISSAO1_END_AT
        )


class ItemVenda(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    venda = models.ForeignKey(
        Venda, on_delete=models.PROTECT, related_name="itensvenda"
    )
    quantidade = models.IntegerField()
    preco_item_unidade = models.FloatField(default=0)
    comissao_vendedor = models.FloatField(default=0)

    MAX_COMISSAO_MADRUGADA_MANHA = 0.05
    MIN_COMISSAO_TARDE_NOITE = 0.04

    def save(self, *args, **kwargs):
        self.comissao_vendedor = self.get_comissao_item()
        return super().save(*args, *kwargs)

    def get_comissao_item(self):
        return self.get_preco_total_item() * self.get_comissao_item_por_horario()

    def get_preco_total_item(self):
        return self.quantidade * self.preco_item_unidade

    def get_comissao_item_por_horario(self):
        if self.venda.is_venda_efetuada_madrugada_manha():
            return self.get_calculo_comissao_madrugada_manha()
        return self.get_calculo_comissao_tarde_noite()

    def get_calculo_comissao_madrugada_manha(self):
        if self.item.get_percentual_comissao() >= self.MAX_COMISSAO_MADRUGADA_MANHA:
            return self.MAX_COMISSAO_MADRUGADA_MANHA
        return self.item.get_percentual_comissao()

    def get_calculo_comissao_tarde_noite(self):
        if self.item.get_percentual_comissao() <= self.MIN_COMISSAO_TARDE_NOITE:
            return self.MIN_COMISSAO_TARDE_NOITE
        return self.item.get_percentual_comissao()
