import factory

from core.tests.factories.produto_factory import ProdutoFactory
from core.product.models.linha_de_produto_model import LinhaDeProduto



class LinhaDeProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LinhaDeProduto
    
    produto = factory.SubFactory(ProdutoFactory)
    preco = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    sku = factory.Faker('pystr', min_chars=10, max_chars=10)
    estoque = factory.Faker('random_int', min=0, max=100)
