from rest_framework.routers import DefaultRouter

from .api.api_item import ItemViewSet, ProdutoViewSet, ServicoViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet, basename="produto")
router.register(r"servicos", ServicoViewSet, basename="servico")
router.register(r"itens", ItemViewSet, basename="item")

urlpatterns = router.urls
