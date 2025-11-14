from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Emprestimo
from ..serializers.emprestimo_serializer import EmprestimoSerializer

"""
Cadastrar usuario - (POST)
cadastrar livro - (POST)
Criar emprestimo - (POST)
listar emprestimos - (GET)
listar usuario - (GET)
listar livro - (GET)
atualizar emprestimo - (PUT)
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
