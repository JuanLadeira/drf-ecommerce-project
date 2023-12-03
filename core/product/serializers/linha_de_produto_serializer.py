from rest_framework import serializers
from core.product.models.linha_de_produto_model import LinhaDeProduto


class LinhaDeProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinhaDeProduto
        fields = "__all__"
