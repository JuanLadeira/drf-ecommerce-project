from rest_framework import serializers

from .models import Categoria, Marca, Produto, ProdutoLine


class CategoriaSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source="nome")
    class Meta:
        model = Categoria
        fields = ("categoria_nome",)


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nome',)


class ProdutoLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoLine
        exclude = ('id','product', 'is_active')

class ProdutoSerializer(serializers.ModelSerializer):
    marca_nome = serializers.CharField(source='marca.nome')
    categoria_nome = serializers.CharField(source='categoria.nome')
    product_line = ProdutoLineSerializer(many=True)

    class Meta:
        model = Produto
        fields = ('nome', 'slug', 'descricao', 'marca_nome', 'categoria_nome', 'product_line')