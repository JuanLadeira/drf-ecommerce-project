from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch

from core.product.models.produto_model import Produto
from core.product.serializers.produto_serializer import ProdutoSerializer
# Create your views here.



class ProdutoViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todos os Produtos
    """
    queryset = Produto.objects.all()
    lookup_field = 'slug'
    
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
                    name='slug', 
                    type=OpenApiTypes.STR, 
                    location=OpenApiParameter.PATH, 
                    description="slug da categoria"),
            ]
    )
    @action(
        detail=False, methods=['get'],
        url_path=r"categoria/(?P<slug>\w+)/all"
    )
    def list_product_by_category_slug(self, request, slug=None):
        """
        Recurso para Listar produtos por categoria
        """
        serializer = ProdutoSerializer(
            self.queryset.filter(categoria__slug=slug).select_related("marca", "categoria"), many=True
            )
        return Response(serializer.data)
    
    @extend_schema(
            summary="Recuperar um produto",
            description="Retorna um produto",
            responses={
                200: ProdutoSerializer,
                404: {"description": "Produto não encontrado", "content": {"application/json": {"example": {"message": "Produto não encontrado"}}}}
            },
            parameters=[
                OpenApiParameter(
                    name='slug', 
                    type=OpenApiTypes.STR, 
                    location=OpenApiParameter.PATH, 
                    description="SLUG do produto"),
            ]
    )
    def retrieve(self, request, slug=None):
        """
        Recurso para recuperar um produto
        """
        serializer = ProdutoSerializer(
            self.queryset.filter(slug=slug)
            .select_related("marca", "categoria")
            .prefetch_related(Prefetch("linhas_de_produto__produto_image")),
            many=True
        )
        return Response(serializer.data)
