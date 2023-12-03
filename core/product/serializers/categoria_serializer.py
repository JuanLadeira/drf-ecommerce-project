from rest_framework import serializers
from core.product.models.categoria_model import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='nome')
    class Meta:
        model = Categoria
        fields = '__all__'

