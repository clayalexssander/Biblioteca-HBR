from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Emprestimo, Livro
from ..serializers.emprestimo_serializer import EmprestimoSerializer
from ..serializers.livro_serializer import LivroSerializer

from django.utils import timezone 
from pytz import timezone as tz
from django.db import transaction
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

@api_view(['POST'])
def devolver_emprestimo(request, pk):
    if request.method == 'POST':
        
        fuso_horario_sp = tz('America/Sao_Paulo')
        timezone.activate(fuso_horario_sp)

        try:
            emprestimo = Emprestimo.objects.get(pk=pk)
        except Emprestimo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if emprestimo.status == "Finalizado":
            timezone.deactivate()
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():

                emprestimo.data_dev = timezone.localtime(timezone.now()).date()
                emprestimo.status = 'Finalizado'
                emprestimo.save()
                
                livro = Livro.objects.get(pk=emprestimo.id_livro_id)
                livro.disponivel = "Disponível"
                livro.save()
                
        except Livro.DoesNotExist:
            timezone.deactivate()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        timezone.deactivate()
        
        return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
        