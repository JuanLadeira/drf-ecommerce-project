from rest_framework.routers import DefaultRouter
from django.urls import include, path
from core.product.views.categoria_view import CategoriaViewSet
from core.product.views.produto_view import ProdutoViewSet

router = DefaultRouter()

router.register(r"categoria", CategoriaViewSet)
router.register(r"produto", ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls))    
]
