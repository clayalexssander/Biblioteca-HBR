from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Livro, Emprestimo
from ..serializers.livro_serializer import LivroSerializer

@api_view(['GET'])
def listar_livros(request):

    if request.method == 'GET':

        consulta = Livro.objects.all()
        # /livros/?titulo=python&ano=2020 para lembrar
        titulo = request.query_params.get('titulo') if hasattr(request, 'query_params') else request.GET.get('titulo')
        ano = request.query_params.get('ano') if hasattr(request, 'query_params') else request.GET.get('ano')

        if titulo:
            consulta = consulta.filter(titulo__icontains=titulo)

        if ano:
            try:
                ano_int = int(ano)
            except (TypeError, ValueError):
                return Response({'ano': ['Ano deve ser um número inteiro.']}, status=status.HTTP_400_BAD_REQUEST)
            consulta = consulta.filter(ano=ano_int)

        serializer = LivroSerializer(consulta, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cadastrar_livro(request):
    if request.method == 'POST':
        dados_livro = request.data

        serializer = LivroSerializer(data=dados_livro)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def livro_detalhe(request, pk):
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    if request.method in ('PUT', 'PATCH'):
        parcial = request.method == 'PATCH'
        serializer = LivroSerializer(livro, data=request.data, partial=parcial)
        if serializer.is_valid():
            # checar mudanças no campo 'disponivel' para evitar inconsistências
            novo_disponivel = serializer.validated_data.get('disponivel', None)
            if novo_disponivel is not None:
                # existem empréstimos não finalizados para esse livro?
                emprestimos_ativos = Emprestimo.objects.filter(id_livro=livro).exclude(status=Emprestimo.Status.FINALIZADO)

                if novo_disponivel == Livro.Disponibilidade.DISPONIVEL and emprestimos_ativos.exists():
                    return Response({'disponivel': ['Não é possível marcar disponível: existem empréstimos em andamento.']}, status=status.HTTP_400_BAD_REQUEST)

                if novo_disponivel == Livro.Disponibilidade.EMPRESTADO and not emprestimos_ativos.exists():
                    return Response({'disponivel': ['Não é possível marcar emprestado sem um empréstimo associado. Use o endpoint de empréstimos.']}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)
