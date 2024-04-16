from rest_framework import viewsets
from product.models.carrinho_model import Carrinho, CarrinhoItem
from product.serializers.carrinho_item_serializer import CarrinhoItemSerializer
from product.serializers.carrinho_serializer import CarrinhoSerializer
from product.utils import generate_session_id

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

    def get_queryset(self):
        sessao_id = self.request.COOKIES.get('sessao_id')
        usuario = self.request.user if self.request.user.is_authenticated else None
        
        if usuario:
            return Carrinho.objects.filter(usuario=usuario)
        elif sessao_id:
            return Carrinho.objects.filter(sessao_id=sessao_id)
        else:
            return Carrinho.objects.none()

    def perform_create(self, serializer):
        sessao_id = self.request.COOKIES.get('sessao_id')
        usuario = self.request.user if self.request.user.is_authenticated else None
        
        if usuario:
            serializer.save(usuario=usuario)
        elif sessao_id:
            serializer.save(sessao_id=sessao_id)
        else:
            # Handle the case where there's neither a user nor a session id
            raise Exception("No session id or user found for the cart")

    def create(self, request, *args, **kwargs):
        # Ensure that a session id exists for anonymous users
        if not request.user.is_authenticated and not request.COOKIES.get('sessao_id'):
            response = super().create(request, *args, **kwargs)
            sessao_id = generate_session_id()
            response.set_cookie('sessao_id', sessao_id, max_age=1209600)  # 2 weeks
            return response
        return super().create(request, *args, **kwargs)
