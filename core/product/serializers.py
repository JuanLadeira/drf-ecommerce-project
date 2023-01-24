from rest_framework import serializers

from .models import Categoria, Marca, Produto


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
