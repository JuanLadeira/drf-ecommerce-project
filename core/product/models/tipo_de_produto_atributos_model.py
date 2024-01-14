# from django.db import models
# from core.product.models.tipo_de_produto_model import TipoDeProduto
# from core.product.models.atributo_model import Atributo

# # Create your models here.

# class TipoDeProdutoAtributos(models.Model):
#     """Classe que representa a relação entre Tipo de produto e atributos"""
#     atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE, related_name="tipo_de_produto_atributos_at", help_text="Atributo")
#     tipo_de_produto = models.ForeignKey(TipoDeProduto, on_delete=models.CASCADE, related_name="tipo_de_produto_atributos_tp", help_text="Tipo de produto")
    

#     class Meta:
#         unique_together = ['atributo', 'tipo_de_produto']