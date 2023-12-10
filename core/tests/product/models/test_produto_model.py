import pytest

pytestmark = pytest.mark.django_db 


class TestProdutoModels:
    def test_produto_output_string(self, produto_factory):
        produto = produto_factory(nome="test_prod")
        assert produto.__str__() == "test_prod"