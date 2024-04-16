from rest_framework import serializers
from core.product.models.item import Item
from core.product.serializers.produto_imagem_serializer import ProdutoImagemSerializer


class ItemSerializer(serializers.ModelSerializer):
    produto_imagem = ProdutoImagemSerializer(many=True, allow_empty=True)
    class Meta:
        model = Item
        fields = [
            'preco',
            'sku',
            "estoque",
            "order",
            'produto_imagem',
        ]
