from django.contrib import admin

from core.product.models.categoria_model import Categoria
from core.product.models.marca_model import Marca
from core.product.models.produto_model import Produto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Marca)