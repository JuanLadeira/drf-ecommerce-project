from rest_framework import serializers
from core.product.models.produto_image_model import ProdutoImage


class ProdutoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoImage
        exclude = ('id',)