from django.contrib import admin
from vendas.models.vendedor import Vendedor
from vendas.models.venda import ItemVenda, Venda


class VendaInline(admin.TabularInline):
    model = Venda.itens.through
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    inlines = [VendaInline]


admin.site.register(Vendedor)
admin.site.register(Venda, VendaAdmin)
