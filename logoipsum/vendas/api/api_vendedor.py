from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from vendas.filters.comissao_filter import ComissoesFilter

from vendas.serializers.comissao_serializer import ComissaoSerializer


from vendas.models.vendedor import Vendedor
from vendas.serializers.vendedor_serializer import VendedorSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    @action(detail=True, methods=["GET"])
    def comissoes(self, request, pk):
        vendas_filtered = ComissoesFilter(
            request.query_params, self.get_object().venda_set.all()
        )
        serializer = ComissaoSerializer(vendas_filtered.qs.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
