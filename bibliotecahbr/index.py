import requests

# cadastro de livros
print("\n----------------------")
print(" Cadastro de Livro ")
print("----------------------")

url_cadastroLivro = "http://127.0.0.1:8000/api/livros/cadastrar?format=json"

titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
ano = int(input("Digite o ano do livro: "))
isbn = input("Digite o ISBN do livro: ")

dados = {
"titulo": titulo,
"autor": autor,
"ano": ano,
"isbn": isbn
}

response = requests.post(url_cadastroLivro, json=dados)

print("Status:", response.status_code)
print("Resposta:", response.json())



# listar todos os livros 
print("\n---------------------------")
print(" Lista de Livros Cadastrados ")
print("-----------------------------")

url_listarLivro ="http://127.0.0.1:8000/api/listar_livros?format=json"
response = requests.get(url_listarLivro)
livros = response.json()

for livro in livros:
 print(f"ID: {livro['id_livro']}")
 print(f"Título: {livro['titulo']}") 
 print(f"Autor: {livro['autor']}")
 print(f"Ano: {livro['ano']}")
 print(f"ISBN: {livro['isbn']}")
 print(f"Disponível: {livro['disponivel']}")


print(response.json())
print("Resposta:",response.status_code)


# lista livros por id

print("\n-------------------------------------")
print(" Pesquisa de Livros Cadastrados por ID")
print("---------------------------------------")

id_livro = input("Digite o ID do livro que deseja procurar: ")

url_listarLivroId = f"http://127.0.0.1:8000/api/livros/{id_livro}/"

response = requests.get(url_listarLivroId)

livro = response.json()
print("ID:", livro["id_livro"])
print("Título:", livro["titulo"])
print("Autor:", livro["autor"])
print("Ano:", livro["ano"])
print("ISBN:", livro["isbn"])
print("Disponibilidade:", livro["disponivel"])

print(response.json())
print("Resposta:",response.status_code)


# atualizar livro

print("\n-------------------------------------")
print(" Atualização dos dados dos Livros")
print("---------------------------------------")

id_livro = input("Digite o ID do livro: ")

url_Atualizarlivro = f"http://127.0.0.1:8000/api/livros/{id_livro}/"

response = requests.get(url_Atualizarlivro)

if response.status_code != 200:
    print("Livro não encontrado.")
else:
    livro = response.json()

novo_titulo = input(f"Título ({livro['titulo']}): ") or livro['titulo']
novo_autor = input(f"Autor ({livro['autor']}): ") or livro['autor']
novo_ano = input(f"Ano ({livro['ano']}): ") or livro['ano']
novo_isbn = input(f"ISBN ({livro['isbn']}): ") or livro['isbn']

dados = {
  "titulo": novo_titulo,
  "autor": novo_autor,
  "ano": int(novo_ano),
  "isbn": novo_isbn
 }

response = requests.put(url_Atualizarlivro, json=dados)
print("Status:", response.status_code)
print("Resposta:", response.json())



# deletar livro 

print("\n----------------------")
print(" Exclusão de livros ")
print("----------------------")

id_livro = input("Digite o ID do livro que deseja excluir: ")

url_DeletarLivro = f"http://127.0.0.1:8000/api/livros/{id_livro}/"

response = requests.delete(url_DeletarLivro)

print("\nResultado")
print("Status:", response.status_code)



# Cadastrar Usuario 

url_cadastroUsuario = "http://127.0.0.1:8000/api/usuarios/cadastrar/"

print("\n----------------------")
print(" Cadastro de Usuário ")
print("----------------------")

nome = input("Digite o nome do usuario: ")
matricula = input("Digite o número de matricula: ")
email = input("Digite o Email: ")

dados = {
  "nome": nome,
  "matricula": matricula,
  "email": email
}

response = requests.post(url_cadastroUsuario, json=dados)
print("Usuário cadastrado com sucesso.")
print(response.json())


# Listar Usuario pelo ID

print("\n--------------------------")
print(" Listar Usuario por ID")
print("--------------------------")

id_usuario = input("Digite o ID do usuario: ")

url_listarUsuario= f"http://127.0.0.1:8000/api/usuarios/{id_usuario}"

response = requests.get(url_listarUsuario)

usuario = response.json()
print("ID:", usuario["id_usuario"])
print("Nome:", usuario["nome"])
print("Matricula:", usuario["matricula"])
print("Email:", usuario["email"])


# Atualizar Usuario
print("\n-------------------------------------")
print(" Atualização dos dados dos Usuários")
print("-------------------------------------")

id_usuario = input("Digite o ID do Usuário: ")

url_AtualizarUsuario = f"http://127.0.0.1:8000/api/usuarios/{id_usuario}/atualizar"


response = requests.get(url_AtualizarUsuario)

if response.status_code != 200:
    print("Usuário não encontrado.")
    exit()

usuario = response.json()


novo_nome = input(f"Nome ({usuario['nome']}): ") or usuario["nome"]
nova_matricula = input(f"Matrícula ({usuario['matricula']}): ") or usuario["matricula"]
novo_email = input(f"Email ({usuario['email']}): ") or usuario["email"]

dados = {
  "nome": novo_nome,
  "matricula": nova_matricula,
  "email": novo_email
}

response = requests.put(url_AtualizarUsuario, json=dados)

print("Status:", response.status_code)
print("Resposta:", response.json())


