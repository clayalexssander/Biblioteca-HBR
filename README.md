# Biblioteca-HBR
Projeto final para curso de capacitação em backend com Python

Python 3.13.7
pip install -r requirements.txt

alterar a senha do banco de dados no settings.py

abrir o workbench e criar um schema chamado biblioteca

cd bibliotecahbr

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/listar_livros

http://127.0.0.1:8000/api/livros/cadastrar



---
# Road map do desenvolvimento

## O que falta
- [ ] Testar os endpoints, eu dei uma testada básica só
- [ ] Atualizar usuário - (PATCH ou PUT depende do método que o usuário requisitar), pode fazer em funções diferentes se quiser, mas ai vai ter que alterar no front qual endpoint da api está sendo usado
- [x] Fazer a data ser apresentada como dia/mes/ano, estou pegando o dado bruto da api e mostrando, tem que resolver no view do frontend
- [x] Apresenta o no listar empréstimos do fronend o nome do usuário e o titulo do livro também, ele só mostra o id e não dá pra ter um noção de qual livro está se referindo
- [ ] Popular o banco de dados, acho que tem como fazer um 'command', mas eu não pesquisei sobre ainda, dá pra pedir uns livros pra IA

## Front-end
- [x] Menu

- [x] Cadastro de usuário
	- Pedir as infos para o usuário e fazer uma requisição POST para criar um usuário
- [x] Mostrar usuário específico
	- Pedir o id e mostrar todas as infos do usuário com aquele id, fazer uma requisição GET
- [x] Atualizar usuário
	- Pedir o id do usuário, fazer uma requisição GET (para ver se esse usuário existe) e pedir as informações novas do usuário
- [x] Deletar usuário
	- Pedir o id do usuário que vai ser deletado, fazer uma requisição DELETE
- [x] Listagem de todos os usuário
	- Fazer uma requisição GET e mostrar todos os usuários
 ---
- [x] Cadastro de livro
	- Pedir as infos do livro  e fazer uma requisição POST para criar um livro
- [x] Mostrar livro específico
	- Pedir o id e mostrar todas as infos do livro com aquele id, fazer uma requisição GET
- [x] Atualizar livro
	- Pedir o id do ivro, fazer uma requisição GET (para ver se esse livro existe) e pedir as informações novas do livro
- [x] Deletar livro
	- Pedir o id do livro que vai ser deletado, fazer uma requisição DELETE
- [x] Listagem de todos os livros
	- Fazer uma requisição GET e mostrar todos os livros
---
- [x] Cadastro de emprestimo
	- Pedir as infos (id do livro e id do usuário) e fazer uma requisição POST para criar um emprestimo
- [x] Mostrar emprestimo específico
	- Pedir o id e mostrar todas as infos do emprestimo com aquele id, fazer uma requisição GET
- [x] Atualizar emprestimo
	- Pedir o id do empréstimo, fazer uma requisição GET (para ver se esse empréstimo existe) e pedir as informações novas do empréstimo
- [x] Deletar livro
	- Pedir o id do livro, fazer um requisição GET (para ver se esse livro existe) e fazer um requisição DELETE
- [x] Devolução de emprestimo
	- Pedir o id do empréstimo, fazer uma requisição GET (para ver se esse empréstimo existe) e fazer uma requisição PATCH
- [x] Listagem de todos os empréstimos
	- Fazer uma requisição GET e mostrar todos os empréstimos

- [ ] 
---

## Back-end

- [x] Cadastrar usuário - (POST) - dg
- [x] Mostrar usuário específico - (GET)
- [x] Deletar usuário - (DELETE)
	- se deletar o user deve deletar o emprestimo e dar upodate status do livro
- [x] Listar todos os usuários - (GET) - DG

---

- [x] Cadastrar livro - (POST) - alex
	- Inserir todos os campos menos o status
- [x] Mostrar livro específico - (GET)
- [x] Atualizar livro - (PATCH)
	- atualiza tudo menos status
- [x] Deletar livro - (DELETE)
	- deleter emprestimos  ligados a esse livro
- [x] Listar todos os livros - (GET) - kauã

---

- [x] Cadastrar emprestimo - (POST) - alex
	- entrar com o ID do livro e Usuario
- [x] Mostrar empréstimo específico - (GET) - alex
- [x] Atualizar empréstimo específico- (PATCH)
	-  o user atualiza apenas o campo de status de: em andamento para finalizado & atrasado para finalizado
- [x] Deletar empréstimo - (DELETE)
 -  se em andamento dar update no status do livro para disponivel
- [x] Realizar devolução do empréstimo - (PATCH) - kauã
- [x] Listar todos os empréstimos - (GET) - kauã



