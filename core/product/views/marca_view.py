from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from core.product.models.marca_model import Marca
from core.product.serializers.marca_serializer import MarcaSerializer




class MarcaViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todas as Marcas
    """
    queryset = Marca.objects.all()

    @extend_schema(responses=MarcaSerializer)
    def list(self, request):
        serializer = MarcaSerializer(self.queryset, many=True)
        return Response(serializer.data)