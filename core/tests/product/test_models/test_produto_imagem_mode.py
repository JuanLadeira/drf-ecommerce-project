import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestProdutoImagemModel:
    def test_marca_output_string(self, produto_imagem_factory , linha_de_produto_factory):
        obj = produto_imagem_factory(url="test.jpg",linha_de_produto=linha_de_produto_factory())
        assert obj.__str__() == obj.ordem
