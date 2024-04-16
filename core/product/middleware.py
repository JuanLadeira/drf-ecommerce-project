from django.utils.deprecation import MiddlewareMixin
from product.utils import generate_session_id


class CarrinhoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        sessao_id = request.COOKIES.get('sessao_id')
        if not sessao_id:
            # Geração de um novo sessao_id
            sessao_id = generate_session_id()
            # Armazenar sessao_id na requisição para uso durante o processamento da requisição
            request.sessao_id = sessao_id
        else:
            # Se já existe sessao_id, apenas armazenar na requisição
            request.sessao_id = sessao_id

    def process_response(self, request, response):
        # Verificar se o sessao_id foi definido na requisição e se ainda não existe no cookie
        if hasattr(request, 'sessao_id') and not request.COOKIES.get('sessao_id'):
            # Definir o cookie de sessao_id com um tempo de expiração
            response.set_cookie('sessao_id', request.sessao_id, max_age=1209600)  # 2 weeks
        return response