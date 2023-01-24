import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import CategoriaFactory, MarcaFactory, ProdutoFactory

register(CategoriaFactory)
register(MarcaFactory)
register(ProdutoFactory)

@pytest.fixture
def api_client():
    return APIClient