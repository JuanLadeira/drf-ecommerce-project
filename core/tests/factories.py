import factory

from core.product.models.categoria_model import Categoria
from core.product.models.marca_model import Marca
from core.product.models.produto_model import Produto


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria
    
    nome = factory.Sequence(lambda n: f"Categoria_{n}")

class MarcaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marca
    
    nome = factory.Sequence(lambda n: f"Marca_{n}")

class ProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Produto
    
    nome = "test_produto"
    descricao = "test_descrição"
    marca = factory.SubFactory(MarcaFactory)
    categoria = factory.SubFactory(CategoriaFactory)
