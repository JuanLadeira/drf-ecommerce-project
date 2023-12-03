from rest_framework import serializers
from core.product.models.produto_model import Produto
from core.product.serializers.categoria_serializer import CategoriaSerializer
from core.product.serializers.marca_serializer import MarcaSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    categoria = CategoriaSerializer()
    class Meta:
        model = Produto
        fields = "__all__"
