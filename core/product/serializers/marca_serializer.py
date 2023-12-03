from rest_framework import serializers
from core.product.models.marca_model import Marca


class MarcaSerializer(serializers.ModelSerializer):
    marca_nome = serializers.CharField(source='nome')
    class Meta:
        model = Marca
        fields = '__all__'