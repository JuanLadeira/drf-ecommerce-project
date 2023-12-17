from rest_framework import serializers
from core.product.models.atributo_valor_model import AtributoValor
from core.product.serializers.atributo_serializer import AtributoSerializer


class AtributoValorSerializer(serializers.ModelSerializer):
    atributo = AtributoSerializer(many=False)
    class Meta:
        model = AtributoValor
        fields = ["att_valor", "atributo"]

