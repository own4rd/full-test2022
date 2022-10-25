from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.api_vendedor import VendedorViewSet
from .api.api_venda import VendaViewSet


router = DefaultRouter()
router.register(r"vendedores", VendedorViewSet, basename="vendedor")
router.register(r"vendas", VendaViewSet, basename="venda")

urlpatterns = router.urls
