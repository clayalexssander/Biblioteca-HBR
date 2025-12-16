# 📚 Biblioteca HBR

Projeto final do curso de capacitação em **Backend com Python**.
API REST desenvolvida com **Django + Django Rest Framework** para gerenciamento de usuários, livros e empréstimos.

---

## 🧰 Tecnologias

* Python **3.13.7**
* Django
* Django REST Framework
* MySQL

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Pré-requisitos

* Python 3.13.7 instalado
* MySQL / MySQL Workbench
* Pip atualizado

---

### 2️⃣ Instalação das dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Banco de Dados

1. Abra o **MySQL Workbench**
2. Crie um schema com o nome:

```sql
biblioteca
```

3. No arquivo `settings.py`, altere as credenciais do banco de dados (usuário e senha).

---

### 4️⃣ Execução do projeto

Entre na pasta do projeto:

```bash
cd bibliotecahbr
```

Execute os comandos abaixo, **na ordem**:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Comando para rodar o servidor: python manage.py runserver
```

---

## 🔐 Acessos

* **Admin Django:**
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

* **Listar livros:**
  [http://127.0.0.1:8000/api/listar_livros](http://127.0.0.1:8000/api/listar_livros)

* **Cadastrar livro:**
  [http://127.0.0.1:8000/api/livros/cadastrar](http://127.0.0.1:8000/api/livros/cadastrar)

---

## 🧪 Popular e Resetar o Banco de Dados

Foi criado um **command personalizado** para popular o banco com dados iniciais (usuários, livros e empréstimos).

### ▶️ Popular o banco

```bash
python manage.py populate_db
```

> Cria aproximadamente:
>
> * 3 usuários
> * 3 livros
> * 2 empréstimos

### 🔄 Resetar o banco

```bash
python manage.py flush
```

> Remove todos os dados do banco (⚠️ use com cuidado).

---

## 🗂️ Modelo do Banco de Dados

<img width="819" height="277" alt="image" src="https://github.com/user-attachments/assets/f4b805a7-b9fa-405e-a721-609349df2a6b" />


---

## 🎨 Front-end

### Usuário

* [x] Menu
* [x] Cadastro de usuário (POST)
* [x] Mostrar usuário específico (GET)
* [x] Atualizar usuário (GET + PATCH)
* [x] Deletar usuário (DELETE)
* [x] Listar todos os usuários (GET)

---

### Livro

* [x] Cadastro de livro (POST)
* [x] Mostrar livro específico (GET)
* [x] Atualizar livro (GET + PATCH)
* [x] Deletar livro (DELETE)
* [x] Listar todos os livros (GET)

---

### Empréstimo

* [x] Cadastro de empréstimo (POST)
* [x] Mostrar empréstimo específico (GET)
* [x] Atualizar empréstimo (GET + PATCH)
* [x] Deletar empréstimo (DELETE)
* [x] Realizar devolução (PATCH)
* [x] Listar todos os empréstimos (GET)

---

## ⚙️ Back-end

### Usuário

* [x] Cadastrar usuário (POST)
* [x] Mostrar usuário específico (GET)
* [x] Listar todos os usuários (GET)
* [x] Deletar usuário (DELETE)

  * Remove empréstimos vinculados
  * Atualiza status dos livros

---

### Livro

* [x] Cadastrar livro (POST)
* [x] Mostrar livro específico (GET)
* [x] Atualizar livro (PATCH)
* [x] Deletar livro (DELETE)

  * Remove empréstimos relacionados
* [x] Listar todos os livros (GET)

---

### Empréstimo

* [x] Cadastrar empréstimo (POST)
* [x] Mostrar empréstimo específico (GET)
* [x] Atualizar empréstimo (PATCH)

  * Status: em andamento → finalizado
  * Status: atrasado → finalizado
* [x] Deletar empréstimo (DELETE)

  * Atualiza status do livro para disponível
* [x] Realizar devolução (PATCH)
* [x] Listar todos os empréstimos (GET)

---

## ✅ Observações Finais

Projeto funcional, organizado e pronto para evolução.
