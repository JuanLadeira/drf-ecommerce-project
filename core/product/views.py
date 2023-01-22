from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Categoria, Marca, Produto
from .serializers import (CategoriaSerializer, MarcaSerializer,
                          ProdutoSerializer)

# Create your views here.

class CategoriaViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir categorias
    """
    queryset = Categoria.objects.all()

    def list(self, request):
        serializer = CategoriaSerializer(self.queryset, many=True)
        return Response(serializer.data)


class MarcaViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir Marcas
    """
    queryset = Marca.objects.all()

    def list(self, request):
        serializer = MarcaSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProdutoViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir Produtos
    """
    queryset = Produto.objects.all()

    def list(self, request):
        serializer = ProdutoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    