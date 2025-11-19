from  biblioteca.urls import urlpatterns
import requests

url ="http://127.0.0.1:8000/api/listar_livros?format=json"

response = requests.get(url)


print(response.json())
print("Resposta:",response.status_code)

