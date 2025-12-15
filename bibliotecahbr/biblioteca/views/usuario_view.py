from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Usuario
from ..serializers.usuario_serializer import UsuarioSerializer

@api_view(['GET'])
def listar_usuarios(request):

    if request.method == 'GET':

        consulta = Usuario.objects.all()

        serializer = UsuarioSerializer(consulta, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def usuario_detalhe(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    if request.method in ('PUT', 'PATCH'):
        parcial = request.method == 'PATCH'
        serializer = UsuarioSerializer(usuario, data=request.data, partial=parcial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def cadastrar_usuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            matricula = serializer.validated_data.get('matricula', '')
            if not (isinstance(matricula, str) and len(matricula) == 4 and matricula.isdigit()):
                return Response({'matricula': ['Matricula deve ter 4 dígitos numéricos.']}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)





