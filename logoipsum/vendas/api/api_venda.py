from rest_framework import viewsets

from vendas.models.venda import Venda
from vendas.serializers.venda_serializer import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
