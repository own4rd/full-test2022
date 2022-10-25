from rest_framework import serializers
from vendas.serializers.itemvenda_serializer import ItemVendaSerializer
from vendas.models.venda import ItemVenda, Venda


class VendaSerializer(serializers.ModelSerializer):

    itensvenda = ItemVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = ["id", "data", "vendedor", "cliente", "itensvenda"]

    def create(self, validated_data):
        itensvendas = validated_data.pop("itensvenda")
        instance = Venda.objects.create(**validated_data)
        for itemvenda in itensvendas:
            obj_itemvenda = ItemVenda(
                **itemvenda, preco_item_unidade=itemvenda["item"].preco, venda=instance
            )
            obj_itemvenda.save()
        return instance
