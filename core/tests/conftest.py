import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from core.tests.factories.categoria_factory import CategoriaFactory
from core.tests.factories.produto_factory import ProdutoFactory
from core.tests.factories.linha_de_produto_factory import LinhaDeProdutoFactory
from core.tests.factories.produto_imagem_factory import ProdutoImagemFactory
from core.tests.factories.tipo_de_produto_factory import TipoDeProdutoFactory
from core.tests.factories.atributo_factory import AtributoFactory
from core.tests.factories.atributo_valor_factory import AtributoValorFactory

register(ProdutoImagemFactory)
register(CategoriaFactory)
register(ProdutoFactory)
register(LinhaDeProdutoFactory)
register(TipoDeProdutoFactory)
register(AtributoFactory)
register(AtributoValorFactory)

@pytest.fixture
def api_client():
    return APIClient