from rest_framework import serializers
from produtos.models.produto import Produto
from produtos.models.item import Item


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
