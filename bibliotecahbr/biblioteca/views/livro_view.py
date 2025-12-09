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
