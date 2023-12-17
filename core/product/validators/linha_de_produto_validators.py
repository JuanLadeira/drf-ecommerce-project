from django.core.exceptions import ValidationError
from core.product.models.atributo_model import Atributo


def validate_ordem_unica_para_produto(instance):
    qs = instance.__class__.objects.filter(produto=instance.produto)
    for obj in qs:
        if instance.id != obj.id and instance.order == obj.order:
            raise ValidationError("A ordem da linha de produto deve ser única")
        

def validate_atributos_duplicados(instance):
    qs = instance.__class__.objects.filter(
        atributo_valor=instance.atributo_valor
        ).filter(
            linha_de_produto=instance.linha_de_produto
        ).exists()
    if not qs:
        iqs = Atributo.objects.filter(
            atributo_valor__atributo_linha_de_produto_valor=instance
            ).values_list("id", flat=True)
        
        if instance.atributo_valor.atributo.id in list(iqs):
            raise ValidationError("O atributo já foi adicionado a este produto")