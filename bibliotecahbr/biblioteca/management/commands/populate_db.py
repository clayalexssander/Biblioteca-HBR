from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from biblioteca.models import Usuario, Livro, Emprestimo


class Command(BaseCommand):
    help = 'Popula o banco com dados de exemplo para testes (usuários, livros e empréstimos)'

    def handle(self, *args, **options):
        today = timezone.localdate()

        users_data = [
            {'nome': 'Alice Silva', 'matricula': '0001', 'email': 'alice@example.com'},
            {'nome': 'Bruno Souza', 'matricula': '0002', 'email': 'bruno@example.com'},
            {'nome': 'Carla Lima', 'matricula': '0003', 'email': 'carla@example.com'},
        ]

        created_users = []
        for u in users_data:
            usuario, created = Usuario.objects.get_or_create(
                email=u['email'], defaults={'nome': u['nome'], 'matricula': u['matricula']}
            )
            created_users.append(usuario)

        books_data = [
            {'titulo': 'Clean Code', 'autor': 'Robert C. Martin', 'ano': 2008, 'isbn': '9780132350884'},
            {'titulo': 'The Pragmatic Programmer', 'autor': 'Andrew Hunt', 'ano': 1999, 'isbn': '9780201616224'},
            {'titulo': 'Design Patterns', 'autor': 'Erich Gamma', 'ano': 1994, 'isbn': '9780201633610'},
        ]

        created_books = []
        for b in books_data:
            livro, created = Livro.objects.get_or_create(
                isbn=b['isbn'],
                defaults={
                    'titulo': b['titulo'],
                    'autor': b['autor'],
                    'ano': b['ano'],
                    'disponivel': Livro.Disponibilidade.DISPONIVEL,
                },
            )
            created_books.append(livro)

        # Criar dois empréstimos de exemplo
        # 1) empréstimo em andamento (livro emprestado)
        emp1, created1 = Emprestimo.objects.get_or_create(
            id_usuario=created_users[0],
            id_livro=created_books[0],
            defaults={
                'data_emp': today - timedelta(days=10),
                'dev_prev': today - timedelta(days=3),
                'data_dev': None,
                'status': Emprestimo.Status.ANDAMENTO,
            },
        )
        if created1:
            created_books[0].disponivel = Livro.Disponibilidade.EMPRESTADO
            created_books[0].save()

        # 2) empréstimo já finalizado (livro disponível)
        emp2, created2 = Emprestimo.objects.get_or_create(
            id_usuario=created_users[1],
            id_livro=created_books[1],
            defaults={
                'data_emp': today - timedelta(days=20),
                'dev_prev': today - timedelta(days=13),
                'data_dev': today - timedelta(days=5),
                'status': Emprestimo.Status.FINALIZADO,
            },
        )
        if created2:
            created_books[1].disponivel = Livro.Disponibilidade.DISPONIVEL
            created_books[1].save()

        self.stdout.write(self.style.SUCCESS('População completada:'))
        self.stdout.write(f'  Usuários: {len(created_users)} (ex.: {created_users[0].email})')
        self.stdout.write(f'  Livros: {len(created_books)} (ex.: {created_books[0].titulo})')
        self.stdout.write(f'  Empréstimos: 2 (ex.: ids {emp1.id_emprestimo}, {emp2.id_emprestimo})')
