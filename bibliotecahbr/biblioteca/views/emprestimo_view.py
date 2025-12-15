from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Emprestimo, Livro
from ..serializers.emprestimo_serializer import EmprestimoSerializer
from ..serializers.livro_serializer import LivroSerializer

from django.utils import timezone 
from datetime import timedelta
from django.db import transaction

@api_view(['GET'])
def listar_emprestimos(request):

    if request.method == 'GET':

        consulta = Emprestimo.objects.select_related('id_livro', 'id_usuario').all()

        serializer = EmprestimoSerializer(consulta, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def realizar_emprestimo(request):
    if request.method == 'POST':
        serializer = EmprestimoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        usuario = serializer.validated_data.get('id_usuario')
        livro = serializer.validated_data.get('id_livro')

        if usuario is None or livro is None:
            errors = {}
            if usuario is None:
                errors['id_usuario'] = ['Campo id_usuario é obrigatório.']
            if livro is None:
                errors['id_livro'] = ['Campo id_livro é obrigatório.']
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        data_emp = serializer.validated_data.get('data_emp')
        dev_prev = serializer.validated_data.get('dev_prev')
        # se data_emp não for informada, assumir hoje
        if data_emp is None:
            data_emp = timezone.localtime(timezone.now()).date()
            serializer.validated_data['data_emp'] = data_emp

        if dev_prev is None:
            # data prevista de devolução = data_emp + 7 dias
            dev_prev = data_emp + timedelta(days=7)
            serializer.validated_data['dev_prev'] = dev_prev

        if data_emp > dev_prev:
            return Response({'non_field_errors': ['data_emp deve ser anterior ou igual a dev_prev.']}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                livro_bloqueado = Livro.objects.select_for_update().get(pk=livro.pk)
                if livro_bloqueado.disponivel != Livro.Disponibilidade.DISPONIVEL:
                    return Response({'id_livro': ['Livro não disponível.']}, status=status.HTTP_400_BAD_REQUEST)

                emprestimo = serializer.save()
                livro_bloqueado.disponivel = Livro.Disponibilidade.EMPRESTADO
                livro_bloqueado.save()

            return Response(EmprestimoSerializer(emprestimo).data, status=status.HTTP_201_CREATED)
        except Livro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def devolver_emprestimo(request, pk):
    if request.method == 'POST':
        try:
            emprestimo = Emprestimo.objects.get(pk=pk)
        except Emprestimo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if emprestimo.status == Emprestimo.Status.FINALIZADO:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                emprestimo.data_dev = timezone.localtime(timezone.now()).date()
                emprestimo.status = Emprestimo.Status.FINALIZADO
                emprestimo.save()

                livro = emprestimo.id_livro
                livro.disponivel = Livro.Disponibilidade.DISPONIVEL
                livro.save()

        except Livro.DoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def emprestimo_detalhe(request, pk):
    try:
        emprestimo = Emprestimo.objects.get(pk=pk)
    except Emprestimo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmprestimoSerializer(emprestimo)
        return Response(serializer.data)

    if request.method in ('PUT', 'PATCH'):
        parcial = request.method == 'PATCH'

        with transaction.atomic():
            try:
                emprestimo = Emprestimo.objects.select_for_update().select_related('id_livro').get(pk=pk)
            except Emprestimo.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = EmprestimoSerializer(emprestimo, data=request.data, partial=parcial)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            novo_status = serializer.validated_data.get('status', emprestimo.status)
            status_antigo = emprestimo.status

            data_emp_efetiva = serializer.validated_data.get('data_emp', emprestimo.data_emp)
            dev_prev_efetiva = serializer.validated_data.get('dev_prev', emprestimo.dev_prev)
            if data_emp_efetiva and dev_prev_efetiva and data_emp_efetiva > dev_prev_efetiva:
                return Response({'non_field_errors': ['data_emp deve ser anterior ou igual a dev_prev.']}, status=status.HTTP_400_BAD_REQUEST)

            if novo_status == Emprestimo.Status.FINALIZADO and status_antigo != Emprestimo.Status.FINALIZADO:
                save_kwargs = {}
                if 'data_dev' not in serializer.validated_data or serializer.validated_data.get('data_dev') is None:
                    save_kwargs['data_dev'] = timezone.localtime(timezone.now()).date()

                serializer.save(**save_kwargs)

                # bloquear e atualizar o livro associado
                try:
                    livro_bloqueado = Livro.objects.select_for_update().get(pk=emprestimo.id_livro_id)
                except Livro.DoesNotExist:
                    transaction.set_rollback(True)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                livro_bloqueado.disponivel = Livro.Disponibilidade.DISPONIVEL
                livro_bloqueado.save()

                return Response(serializer.data)

            # se estiver reabrindo um empréstimo que estava finalizado -> marcar livro como emprestado
            if status_antigo == Emprestimo.Status.FINALIZADO and novo_status != Emprestimo.Status.FINALIZADO:
                # se não foi passado data_dev, reseta ela
                if 'data_dev' not in serializer.validated_data:
                    serializer.validated_data['data_dev'] = None

                serializer.save()

                try:
                    livro_bloqueado = Livro.objects.select_for_update().get(pk=emprestimo.id_livro_id)
                except Livro.DoesNotExist:
                    transaction.set_rollback(True)
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                livro_bloqueado.disponivel = Livro.Disponibilidade.EMPRESTADO
                livro_bloqueado.save()

                return Response(serializer.data)

            # apenas salvar alterações no empréstimo
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        if emprestimo.status == Emprestimo.Status.FINALIZADO:
            emprestimo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        try:
            livro = emprestimo.id_livro
        except Livro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            livro.disponivel = Livro.Disponibilidade.DISPONIVEL
            livro.save()
            emprestimo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)