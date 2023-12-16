import pytest

pytestmark = pytest.mark.django_db #PROVIDE THE MARK FOR ALL THE TESTS ACCESS THE DB

class TestCategoriaModels:
    def test_categoria_output_string(self, categoria_factory):
        categoria = categoria_factory()
        assert categoria.__str__() == categoria.nome
