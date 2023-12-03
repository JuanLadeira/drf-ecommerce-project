from rest_framework import serializers
from core.product.models.produto_model import Produto
from core.product.serializers.categoria_serializer import CategoriaSerializer
from core.product.serializers.marca_serializer import MarcaSerializer
from core.product.serializers.linha_de_produto_serializer import LinhaDeProdutoSerializer

#não está sendo utilizado no momento, mas entregaria todos os dados do produto
class ProdutoTotalSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    categoria = CategoriaSerializer()
    linhas_de_produto = LinhaDeProdutoSerializer(many=True)
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoSerializer(serializers.ModelSerializer):
    marca_nome = serializers.CharField(source='marca.nome')
    categoria_nome = serializers.CharField(source='categoria.nome')
    linhas_de_produto = LinhaDeProdutoSerializer(many=True)
    class Meta:
        model = Produto
        fields = "__all__"
