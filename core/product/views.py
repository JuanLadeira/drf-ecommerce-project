from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Categoria, Marca, Produto
from .serializers import (CategoriaSerializer, MarcaSerializer,
                          ProdutoSerializer)

# Create your views here.

class CategoriaViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todas as categorias
    """
    queryset = Categoria.objects.all()

    @extend_schema(responses=CategoriaSerializer)
    def list(self, request):
        serializer = CategoriaSerializer(self.queryset, many=True)
        return Response(serializer.data)


class MarcaViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todas as Marcas
    """
    queryset = Marca.objects.all()

    @extend_schema(responses=MarcaSerializer)
    def list(self, request):
        serializer = MarcaSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProdutoViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todos os Produtos
    """
    queryset = Produto.objects.all()
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProdutoSerializer(self.queryset.filter(slug=slug), many=True)
    
        return Response(serializer.data)
    
    @extend_schema(responses=ProdutoSerializer)
    def list(self, request):
        serializer = ProdutoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"categoria/(?P<categoria>\w+)/all",
        )
    def listar_produto_pela_categoria(self, request, categoria=None):
        """
        Endpoint para retornar produto pelo nome da categoria.
        """
        serializer = ProdutoSerializer(self.queryset.filter(categoria__nome=categoria), many=True)
        return Response(serializer.data)
    