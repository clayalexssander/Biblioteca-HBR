from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.menu, name='menu'),

    # Livros
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/<int:pk>/editar/', views.livro_edit, name='livro_edit'),
    path('livros/<int:pk>/deletar/', views.livro_delete, name='livro_delete'),

    # Usuários
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/novo/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('usuarios/<int:pk>/editar/', views.usuario_edit, name='usuario_edit'),
    path('usuarios/<int:pk>/deletar/', views.usuario_delete, name='usuario_delete'),

    # Empréstimos
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('emprestimos/novo/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/<int:pk>/', views.emprestimo_detail, name='emprestimo_detail'),
    path('emprestimos/<int:pk>/deletar/', views.emprestimo_delete, name='emprestimo_delete'),
    path('emprestimos/<int:pk>/devolver/',views.emprestimo_devolver,name='emprestimo_devolver'),
]
