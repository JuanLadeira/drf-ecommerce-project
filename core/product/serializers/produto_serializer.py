from rest_framework import serializers
from core.product.models.produto_model import Produto
from core.product.serializers.categoria_serializer import CategoriaSerializer
from core.product.serializers.marca_serializer import MarcaSerializer
from core.product.serializers.linha_de_produto_serializer import LinhaDeProdutoSerializer
from core.product.models.atributo_model import Atributo
from core.product.serializers.atributo_serializer import AtributoSerializer
from logging import getLogger


logger = getLogger("django")

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    marca = MarcaSerializer()
    linhas_de_produto = LinhaDeProdutoSerializer(many=True, allow_empty=True)
    atributo = serializers.SerializerMethodField()
    
    class Meta:
        model = Produto
        fields = '__all__'

    def get_atributo(self, obj):
        atributo = Atributo.objects.filter(tipo_de_produto_atributos__produto__id=obj.id)
        logger.debug(f"atributos filtrados pelo get_atributo: {atributo}")
        return AtributoSerializer(atributo, many=True).data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop("atributo")
        attr_values = {}
        for key in av_data:
            attr_values.update({key["id"]: key["name"]})
        data.update({"especificações dos tipos": attr_values})

        return data