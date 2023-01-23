from pytest_factoryboy import register

from .factories import CategoriaFactory, MarcaFactory, ProdutoFactory

register(CategoriaFactory)
register(MarcaFactory)
register(ProdutoFactory)
