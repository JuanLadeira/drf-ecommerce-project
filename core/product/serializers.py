from rest_framework import serializers

from .models import Categoria, Marca, Produto, ProdutoLine


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    categoria = CategoriaSerializer()
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoLineSerializer(serializers.ModelSerializer):
    product = ProdutoSerializer()
    class Meta:
        model = ProdutoLine
        fields = "__all__"