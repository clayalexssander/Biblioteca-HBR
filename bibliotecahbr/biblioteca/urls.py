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
    path('livros/cadastrar', livro_view.cadastar_livro), # cadastrar livros

    path('usuarios/', usuario_view.listar_usuarios), # Listar todos os usuários
    path('usuarios/<int:pk>/deletar', usuario_view.deletar_usuario), # Listar todos os usuários
    
    
    path('emprestimos/', emprestimo_view.listar_emprestimos), # Listar todos os emprestimos
    path('emprestimos/<int:pk>/deletar', emprestimo_view.deletar_emprestimo), # Deletar empréstimo
    path('emprestimos/<int:pk>/devolver', emprestimo_view.devolver_emprestimo), # Devolver empréstimos
    
]
