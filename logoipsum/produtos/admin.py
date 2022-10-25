from django.contrib import admin

from .models.item import Item
from .models.servico import Servico
from .models.produto import Produto

admin.site.register(Item)
admin.site.register(Servico)
admin.site.register(Produto)
