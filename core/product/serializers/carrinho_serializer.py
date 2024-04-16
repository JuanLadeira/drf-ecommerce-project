from rest_framework import serializers
from core.product.models.carrinho_model import Carrinho, CarrinhoItem
from core.product.serializers.carrinho_item_serializer import CarrinhoItemSerializer


class CarrinhoSerializer(serializers.ModelSerializer):
    itens = CarrinhoItemSerializer(many=True)

    class Meta:
        model = Carrinho
        fields = ['itens']