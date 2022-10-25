from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.api_cliente import ClienteViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet, basename="cliente")

urlpatterns = router.urls
