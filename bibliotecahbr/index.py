import requests

# cadastro de livros
url_cadastroLivro = "http://127.0.0.1:8000/api/livros/cadastrar?format=json"

titulo = input("Título: ")
autor = input("Autor: ")
ano = input("Ano: ")
isbn = input("ISBN: ")

dados = {
"titulo": titulo,
"autor": autor,
"ano": int(ano),
"isbn": isbn
}

response = requests.post(url_cadastroLivro, json=dados)

print("Status:", response.status_code)
print("Resposta:", response.json())



# listar todos os livros 
url_listarLivro ="http://127.0.0.1:8000/api/listar_livros?format=json"

response = requests.get(url_listarLivro)

print(response.json())
print("Resposta:",response.status_code)



