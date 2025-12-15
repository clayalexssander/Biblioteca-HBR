from django.contrib import admin
from .views import livro_view, usuario_view, emprestimo_view
from django.urls import path, include
"""
COmo fazer uma URL Restful

OPERAÇÕES CRUD BÁSICAS:
- GET /recurso         -> Listar todos os recursos ou aplicar filtros.
- GET /recurso/{id}    -> Obter um recurso específico.
- POST /recurso        -> Criar um novo recurso.
- PATCH /recurso/{id}  -> Atualizar parcialmente um recurso (ex: mudar título).

"""

urlpatterns = [
    path('livros/', livro_view.listar_livros), # Listar todos os livros
    path('livros/cadastrar', livro_view.cadastrar_livro), # cadastrar livros
    path('livros/<int:pk>/', livro_view.livro_detalhe), # detalhes do livro

    path('usuarios/', usuario_view.listar_usuarios), # Listar todos os usuários
    path('usuarios/cadastrar', usuario_view.cadastrar_usuario), # cadastrar usuário
    path('usuarios/<int:pk>/', usuario_view.usuario_detalhe), # detalhes do usuário
    
    
    path('emprestimos/', emprestimo_view.listar_emprestimos), # Listar todos os emprestimos
    path('emprestimos/realizar', emprestimo_view.realizar_emprestimo), # realizar empréstimo
    path('emprestimos/<int:pk>/', emprestimo_view.emprestimo_detalhe), # detalhes do emprestimo
    path('emprestimos/<int:pk>/devolver', emprestimo_view.devolver_emprestimo), # Devolver empréstimos
    
]
