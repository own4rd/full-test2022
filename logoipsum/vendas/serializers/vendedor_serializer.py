from rest_framework import serializers
from vendas.models.vendedor import Vendedor


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"
