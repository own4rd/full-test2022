from rest_framework import serializers
from vendas.models.venda import ItemVenda


class ItemVendaSerializer(serializers.ModelSerializer):
    # TODO Salvar preco unidade

    preco_item_unidade = serializers.FloatField(read_only=True)

    class Meta:
        model = ItemVenda
        exclude = ["venda"]
