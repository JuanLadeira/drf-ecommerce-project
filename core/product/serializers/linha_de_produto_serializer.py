from rest_framework import serializers
from core.product.models.linha_de_produto_model import LinhaDeProduto
from core.product.serializers.produto_imagem_serializer import ProdutoImagemSerializer
from core.product.serializers.atributo_valor_serializer import AtributoValorSerializer

class LinhaDeProdutoSerializer(serializers.ModelSerializer):
    produto_imagem = ProdutoImagemSerializer(many=True, allow_empty=True)
    atributos = AtributoValorSerializer(many=True, allow_empty=True)
    class Meta:
        model = LinhaDeProduto
        fields = [
            'preco',
            'sku',
            "estoque",
            "order",
            'produto_imagem',
            "atributos",
        ]
