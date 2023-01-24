from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
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
    
    @extend_schema(responses=ProdutoSerializer)
    def list(self, request):
        serializer = ProdutoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    