import factory

from core.product.models.categoria_model import Categoria
from core.product.models.marca_model import Marca
from core.product.models.produto_model import Produto
from core.product.models.item import LinhaDeProduto



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
    slug = factory.Sequence(lambda n: f"slug_{n}")

class LinhaDeProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LinhaDeProduto
    
    produto = factory.SubFactory(ProdutoFactory)
    preço = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    sku = factory.Faker('pystr', min_chars=10, max_chars=10)
    estoque = factory.Faker('random_int', min=0, max=100)
