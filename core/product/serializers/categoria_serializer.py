from rest_framework import serializers
from core.product.models.categoria_model import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
