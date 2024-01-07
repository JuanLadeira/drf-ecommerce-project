import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestTipoDeProdutoModels:
    def test_tipo_de_produto_output_string(self, tipo_de_produto_factory):
        tipo_de_produto = tipo_de_produto_factory()
        assert tipo_de_produto.__str__() == tipo_de_produto.nome


