import requests

# cadastro de livros
url_cadastroLivro = "http://127.0.0.1:8000/api/livros/cadastrar?format=json"

print("\n----------------------")
print(" Cadastro de Livro ")
print("----------------------")

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
url_listarLivro ="http://127.0.0.1:8000/api/listar_livros?format=json"

print("\n---------------------------")
print(" Lista de Livros Cadastrados ")
print("-----------------------------")

response = requests.get(url_listarLivro)

print(response.json())
print("Resposta:",response.status_code)


