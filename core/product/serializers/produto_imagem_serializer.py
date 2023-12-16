from rest_framework import serializers
from core.product.models.produto_imagem_model import ProdutoImagem


class ProdutoImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoImagem
        exclude = ('id',)