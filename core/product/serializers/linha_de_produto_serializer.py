from rest_framework import serializers
from core.product.models.linha_de_produto_model import LinhaDeProduto
from core.product.serializers.produto_image_serializer import ProdutoImageSerializer


class LinhaDeProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinhaDeProduto
        fields = [
            'preco',
            'sku',
            "estoque",
            "order",
            'produto_image',
        ]
