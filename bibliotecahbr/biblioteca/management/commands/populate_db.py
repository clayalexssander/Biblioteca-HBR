from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from biblioteca.models import Usuario, Livro, Emprestimo


class Command(BaseCommand):
    help = 'Popula o banco com dados de exemplo para testes (usuários, livros e empréstimos)'

    def handle(self, *args, **options):
        today = timezone.localdate()

        # --------------------
        # USUÁRIOS
        # --------------------
        users_data = [
            {'nome': 'Alice Silva', 'matricula': '0001', 'email': 'alice@example.com'},
            {'nome': 'Bruno Souza', 'matricula': '0002', 'email': 'bruno@example.com'},
            {'nome': 'Carla Lima', 'matricula': '0003', 'email': 'carla@example.com'},
            {'nome': 'Diego Martins', 'matricula': '0004', 'email': 'diego@example.com'},
            {'nome': 'Elisa Rocha', 'matricula': '0005', 'email': 'elisa@example.com'},
        ]

        created_users = []
        for u in users_data:
            usuario, _ = Usuario.objects.get_or_create(
                email=u['email'],
                defaults={
                    'nome': u['nome'],
                    'matricula': u['matricula']
                }
            )
            created_users.append(usuario)

        # --------------------
        # LIVROS
        # --------------------
        books_data = [
            {'titulo': 'Clean Code', 'autor': 'Robert C. Martin', 'ano': 2008, 'isbn': '9780132350884'},
            {'titulo': 'The Pragmatic Programmer', 'autor': 'Andrew Hunt', 'ano': 1999, 'isbn': '9780201616224'},
            {'titulo': 'Design Patterns', 'autor': 'Erich Gamma', 'ano': 1994, 'isbn': '9780201633610'},
            {'titulo': 'Refactoring', 'autor': 'Martin Fowler', 'ano': 1999, 'isbn': '9780201485677'},
            {'titulo': 'Domain-Driven Design', 'autor': 'Eric Evans', 'ano': 2003, 'isbn': '9780321125217'},
        ]

        created_books = []
        for b in books_data:
            livro, _ = Livro.objects.get_or_create(
                isbn=b['isbn'],
                defaults={
                    'titulo': b['titulo'],
                    'autor': b['autor'],
                    'ano': b['ano'],
                    'disponivel': Livro.Disponibilidade.DISPONIVEL,
                },
            )
            created_books.append(livro)

        # --------------------
        # EMPRÉSTIMOS
        # --------------------

        emprestimos_data = [
            # Empréstimo em andamento
            {
                'usuario': created_users[0],
                'livro': created_books[0],
                'data_emp': today - timedelta(days=7),
                'dev_prev': today - timedelta(days=1),
                'data_dev': None,
                'status': Emprestimo.Status.ANDAMENTO,
                'disponibilidade_livro': Livro.Disponibilidade.EMPRESTADO,
            },

            # Empréstimo finalizado no prazo
            {
                'usuario': created_users[1],
                'livro': created_books[1],
                'data_emp': today - timedelta(days=20),
                'dev_prev': today - timedelta(days=13),
                'data_dev': today - timedelta(days=10),
                'status': Emprestimo.Status.FINALIZADO,
                'disponibilidade_livro': Livro.Disponibilidade.DISPONIVEL,
            },

            # Empréstimo atrasado (ainda em andamento)
            {
                'usuario': created_users[2],
                'livro': created_books[2],
                'data_emp': today - timedelta(days=30),
                'dev_prev': today - timedelta(days=15),
                'data_dev': None,
                'status': Emprestimo.Status.ANDAMENTO,
                'disponibilidade_livro': Livro.Disponibilidade.EMPRESTADO,
            },

            # Empréstimo finalizado com atraso
            {
                'usuario': created_users[3],
                'livro': created_books[3],
                'data_emp': today - timedelta(days=25),
                'dev_prev': today - timedelta(days=18),
                'data_dev': today - timedelta(days=5),
                'status': Emprestimo.Status.FINALIZADO,
                'disponibilidade_livro': Livro.Disponibilidade.DISPONIVEL,
            },

            # Empréstimo recente em andamento
            {
                'usuario': created_users[4],
                'livro': created_books[4],
                'data_emp': today - timedelta(days=2),
                'dev_prev': today + timedelta(days=5),
                'data_dev': None,
                'status': Emprestimo.Status.ANDAMENTO,
                'disponibilidade_livro': Livro.Disponibilidade.EMPRESTADO,
            },
        ]

        emprestimos_criados = 0
        for e in emprestimos_data:
            emp, created = Emprestimo.objects.get_or_create(
                id_usuario=e['usuario'],
                id_livro=e['livro'],
                defaults={
                    'data_emp': e['data_emp'],
                    'dev_prev': e['dev_prev'],
                    'data_dev': e['data_dev'],
                    'status': e['status'],
                },
            )

            if created:
                e['livro'].disponivel = e['disponibilidade_livro']
                e['livro'].save()
                emprestimos_criados += 1

        # --------------------
        # OUTPUT
        # --------------------
        self.stdout.write(self.style.SUCCESS('População completada com sucesso!'))
        self.stdout.write(f'  Usuários: {len(created_users)}')
        self.stdout.write(f'  Livros: {len(created_books)}')
        self.stdout.write(f'  Empréstimos criados: {emprestimos_criados}')
