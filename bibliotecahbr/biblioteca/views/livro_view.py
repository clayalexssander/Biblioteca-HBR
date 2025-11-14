from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Livro
from ..serializers.livro_serializer import LivroSerializer

"""
Cadastrar usuario - (POST) - dg
cadastrar livro - (POST) - alex
Criar emprestimo - (POST) - alex
listar emprestimos - (GET) - alex
listar usuario - (GET) - DG
listar livro - (GET) - kauã
atualizar emprestimo - (PUT) - kauã
"""

# Create your views here.
@api_view(['GET'])
def listar_livros(request):

    if request.method == 'GET':

        queryset = Livro.objects.all()

        if len(queryset) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LivroSerializer(queryset, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)
