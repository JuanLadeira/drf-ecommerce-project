import pytest
from django.core.exceptions import ValidationError
pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestLinhaDeProdutoModels:
    def test_linha_de_produto_output_string(self, linha_de_produto_factory):
        linha_de_produto = linha_de_produto_factory()
        assert linha_de_produto.__str__() == linha_de_produto.sku


    def test_ordem_duplicada_error(self, linha_de_produto_factory, produto_factory):
        obj = produto_factory()
        linha = linha_de_produto_factory(order=1,produto=obj)
        with pytest.raises(ValidationError):
            linha_2 = linha_de_produto_factory(order=1,produto=obj).clean()

        
    def test_numero_automatico_de_ordem(self, linha_de_produto_factory, produto_factory):
        obj = produto_factory()
        linha = linha_de_produto_factory(produto=obj)
        linha_2 = linha_de_produto_factory(produto=obj)
        assert linha_2.order == 2
