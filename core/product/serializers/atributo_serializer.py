from rest_framework import serializers
from core.product.models.atributo_model import Atributo


class AtributoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atributo
        fields = ['name', "id"]

