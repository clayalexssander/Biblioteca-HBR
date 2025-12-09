from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Usuario
from ..serializers.usuario_serializer import UsuarioSerializer

@api_view(['GET'])
def listar_usuarios(request):

    if request.method == 'GET':

        queryset = Usuario.objects.all()

        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_usuario(request, pk):
    
    if request.method == 'DELETE':
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
        
        

