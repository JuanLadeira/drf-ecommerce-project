from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from core.product.models.produto_model import Produto
from core.product.serializers.produto_serializer import ProdutoSerializer
# Create your views here.



class ProdutoViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todos os Produtos
    """
    queryset = Produto.objects.all()
    
    @extend_schema(
            summary="Listar todos os produtos",
            description="Retorna uma lista de produtos",
            responses=ProdutoSerializer
            )
    def list(self, request):
        """
        Recurso para Listar todos os produtos
        """
        serializer = ProdutoSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Listar produtos por categoria",
            description="Retorna uma lista de produtos por categoria",
            responses=ProdutoSerializer,
            parameters=[
                OpenApiParameter(
                    name='categoria', 
                    type=OpenApiTypes.STR, 
                    location=OpenApiParameter.PATH, 
                    description="Nome da categoria"),
            ]
            )
    @action(detail=False, methods=['get'], url_path=r"categoria/(?P<categoria>\w+)/all")
    def list_product_by_category(self, request, categoria=None):
        """
        Recurso para Listar produtos por categoria
        """
        serializer = ProdutoSerializer(
            self.queryset.filter(categoria__nome=categoria), many=True
            )
        return Response(serializer.data)