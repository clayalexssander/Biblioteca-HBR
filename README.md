# Biblioteca-HBR
Projeto final para curso de capacitação em backend com Python

Python 3.13.7
pip install -r requirements.txt

alterar a senha do banco de dados no settings.py

abrir o workbench e criar um schema chamado biblioteca

cd bibliotecahbr

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/listar_livros
---
# Road map do desenvolvimento

## Front-end
- [ ] Menu

- [ ] Cadastro de usuário
	- Pedir as infos para o usuário e fazer uma requisição POST para criar um usuário
- [ ] Mostrar usuário específico
	- Pedir o id e mostrar todas as infos do usuário com aquele id, fazer uma requisição GET
- [ ] Atualizar usuário
	- Pedir o id do usuário, fazer uma requisição GET (para ver se esse usuário existe) e pedir as informações novas do usuário
- [ ] Deletar usuário
	- Pedir o id do usuário que vai ser deletado, fazer uma requisição DELETE
- [ ] Listagem de todos os usuário
	- Fazer uma requisição GET e mostrar todos os usuários
 ---
- [ ] Cadastro de livro
	- Pedir as infos do livro  e fazer uma requisição POST para criar um livro
- [ ] Mostrar livro específico
	- Pedir o id e mostrar todas as infos do livro com aquele id, fazer uma requisição GET
- [ ] Atualizar livro
	- Pedir o id do ivro, fazer uma requisição GET (para ver se esse livro existe) e pedir as informações novas do livro
- [ ] Deletar livro
	- Pedir o id do livro que vai ser deletado, fazer uma requisição DELETE
- [ ] Listagem de todos os livros
	- Fazer uma requisição GET e mostrar todos os livros
---
- [ ] Cadastro de emprestimo
	- Pedir as infos (id do livro e id do usuário) e fazer uma requisição POST para criar um emprestimo
- [ ] Mostrar emprestimo específico
	- Pedir o id e mostrar todas as infos do emprestimo com aquele id, fazer uma requisição GET
- [ ] Atualizar emprestimo
	- Pedir o id do empréstimo, fazer uma requisição GET (para ver se esse empréstimo existe) e pedir as informações novas do empréstimo
- [ ] Deletar livro
	- Pedir o id do livro, fazer um requisição GET (para ver se esse livro existe) e fazer um requisição DELETE
- [ ] Devolução de emprestimo
	- Pedir o id do empréstimo, fazer uma requisição GET (para ver se esse empréstimo existe) e fazer uma requisição PATCH
- [ ] Listagem de todos os empréstimos
	- Fazer uma requisição GET e mostrar todos os empréstimos
---

## Back-end
- [ ] Cadastrar usuário - (POST) - dg
- [ ] Mostrar usuário específico - (GET)
- [ ] Atualizar usuário - (PATCH)
- [ ] Deletar usuário - (DELETE)
- [x] Listar todos os usuários - (GET) - DG
---
- [ ] Cadastrar livro - (POST) - alex
- [ ] Mostrar livro específico - (GET)
- [ ] Atualizar livro - (PATCH)
- [ ] Deletar livro - (DELETE)
- [x] Listar todos os livros - (GET) - kauã
---
- [ ] Cadastrar emprestimo - (POST) - alex
- [ ] Mostrar empréstimo específico - (GET) - alex
- [ ] Atualizar empréstimo específico- (PATCH)
- [ ] Deletar empréstimo - (DELETE)
- [x] Realizar devolução do  empréstimo - (PATCH) - kauã
- [x] Listar todos os empréstimos - (GET) - kauã



