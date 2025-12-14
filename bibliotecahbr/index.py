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


