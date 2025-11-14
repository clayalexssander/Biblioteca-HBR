from django.contrib import admin
from .views import livro_view
from django.urls import path, include

urlpatterns = [
    path('listar_livros', livro_view.listar_livros),
]
