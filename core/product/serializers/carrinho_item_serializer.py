from rest_framework import serializers
from core.product.models.carrinho_model import Carrinho, CarrinhoItem

class CarrinhoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoItem
        fields = ['item', 'quantidade']