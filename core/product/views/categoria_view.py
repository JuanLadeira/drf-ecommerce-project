from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from rest_framework.response import Response

from core.product.models.categoria_model import Categoria

from core.product.serializers.categoria_serializer import CategoriaSerializer


class CategoriaViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todas as categorias
    """
    queryset = Categoria.objects.all().select_related("parent")

    @extend_schema(responses=CategoriaSerializer)
    def list(self, request):
        serializer = CategoriaSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
