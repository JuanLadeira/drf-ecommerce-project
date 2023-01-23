import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestCategoriaModels:
    def test_categoria_output_string(self, categoria_factory):
        categoria = categoria_factory()
        assert categoria.__str__() == "test_categoria"

class TestMarcaModels:
    def test_marca_output_string(self, marca_factory):
        marca = marca_factory()
        assert marca.__str__() == "test_marca"

class TestProdutoModels:
    def test_produto_output_string(self, produto_factory):
        produto = produto_factory(nome="test_prod")
        assert produto.__str__() == "test_prod"