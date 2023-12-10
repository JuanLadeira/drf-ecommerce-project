import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestLinhaDeProdutoModels:
    def test_linha_de_produto_output_string(self, linha_de_produto_factory):
        linha_de_produto = linha_de_produto_factory()
        assert linha_de_produto.__str__() == linha_de_produto.sku
