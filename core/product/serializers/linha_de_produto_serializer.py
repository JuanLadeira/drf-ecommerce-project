from rest_framework import serializers
from core.product.models.linha_de_produto_model import LinhaDeProduto
from core.product.serializers.produto_serializer import ProdutoSerializer


class LinhaDeProdutoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    class Meta:
        model = LinhaDeProduto
        fields = "__all__"
