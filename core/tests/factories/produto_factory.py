import factory

from core.product.models.produto_model import Produto
from core.tests.factories.categoria_factory import CategoriaFactory
from core.tests.factories.marca_factory import MarcaFactory
from core.tests.factories.tipo_de_produto_factory import TipoDeProdutoFactory



class ProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Produto
    
    nome = "test_produto"
    descricao = "test_descrição"
    marca = factory.SubFactory(MarcaFactory)
    categoria = factory.SubFactory(CategoriaFactory)
    slug = factory.Sequence(lambda n: f"slug_{n}")
    tipo_produto = factory.SubFactory(TipoDeProdutoFactory)
