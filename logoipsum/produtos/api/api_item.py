from rest_framework import viewsets
from produtos.models.item import Item
from rest_framework import filters

from produtos.models.produto import Produto
from produtos.models.servico import Servico
from produtos.serializers.produto_serializer import ProdutoSerializer
from produtos.serializers.servico_serializer import ServicoSerializer
from produtos.serializers.item_serializer import ItemSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'id']

    