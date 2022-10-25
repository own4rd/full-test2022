from rest_framework import serializers
from vendas.serializers.itemvenda_serializer import ItemVendaSerializer
from vendas.models.venda import ItemVenda, Venda


class ComissaoSerializer(serializers.ModelSerializer):

    comissao = serializers.SerializerMethodField()
    venda = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields = ["id", "data", "vendedor", "comissao", "venda"]

    def get_comissao(self, obj):
        return obj.calcular_total_comissao()

    def get_venda(self, obj):
        return obj.calcular_total_venda()
