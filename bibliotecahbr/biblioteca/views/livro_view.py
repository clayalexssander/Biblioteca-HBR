from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Livro
from ..serializers.livro_serializer import LivroSerializer

@api_view(['GET'])
def listar_livros(request):

    if request.method == 'GET':

        queryset = Livro.objects.all()

        serializer = LivroSerializer(queryset, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cadastar_livro(request):
    if request.method == 'POST':
        new_livro = request.data

        serializer = LivroSerializer(data=new_livro)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
