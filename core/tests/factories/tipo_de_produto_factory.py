import factory

from core.product.models.tipo_de_produto_model import TipoDeProduto

class TipoDeProdutoFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('pystr', min_chars=10, max_chars=10)


    class Meta:
        model = TipoDeProduto
