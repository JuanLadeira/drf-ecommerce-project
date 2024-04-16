from rest_framework import serializers
from core.product.models.produto_model import Produto
from core.product.serializers.categoria_serializer import CategoriaSerializer
from core.product.serializers.marca_serializer import MarcaSerializer
from core.product.serializers.item_serializer import ItemSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    marca = MarcaSerializer()
    linhas_de_produto = ItemSerializer(many=True, allow_empty=True)
    
    class Meta:
        model = Produto
        fields = '__all__'