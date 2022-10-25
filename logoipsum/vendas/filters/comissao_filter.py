from django_filters import rest_framework as filters

from vendas.models.venda import Venda


class ComissoesFilter(filters.FilterSet):
    """
    Para aplicar filtro:
    http://.../?data_after=2016-01-01&data_before=2016-02-01
    """

    data = filters.DateFromToRangeFilter()

    class Meta:
        model = Venda
        fields = ["data"]
