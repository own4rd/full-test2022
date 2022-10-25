from rest_framework import viewsets

from clientes.models.cliente import Cliente
from clientes.serializers.cliente_serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
