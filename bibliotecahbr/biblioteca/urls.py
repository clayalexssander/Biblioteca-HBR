from django.contrib import admin
from .views import livro_view, usuario_view, emprestimo_view
from django.urls import path, include

urlpatterns = [
    path('listar_livros', livro_view.listar_livros),
    path('devolver_emprestimo/<int:pk>', emprestimo_view.devolver_emprestimo)
]
