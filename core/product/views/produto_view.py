from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from core.product.models.produto_model import Produto


from core.product.serializers.produto_serializer import ProdutoSerializer
# Create your views here.



class ProdutoViewSet(viewsets.ViewSet):
    """
    Uma simples viewset para exibir todos os Produtos
    """
    queryset = Produto.objects.all()
    
    @extend_schema(responses=ProdutoSerializer)
    def list(self, request):
        serializer = ProdutoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    