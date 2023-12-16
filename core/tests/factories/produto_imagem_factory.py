import factory

from core.product.models.produto_imagem_model import ProdutoImagem

from core.tests.factories.linha_de_produto_factory import LinhaDeProdutoFactory




class ProdutoImagemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProdutoImagem
    
    nome = "test_produto"
    linha_de_produto = factory.SubFactory(LinhaDeProdutoFactory)
    alternative_text = factory.Faker('pystr', min_chars=10, max_chars=10)
    url = factory.Faker('pystr', min_chars=10, max_chars=10)
    is_active = factory.Faker('pybool')
    alternative_text = factory.Faker('pystr', min_chars=10, max_chars=10)
