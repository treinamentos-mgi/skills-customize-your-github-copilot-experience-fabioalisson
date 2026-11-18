# 📘 Atividade: Criando APIs REST com FastAPI

## 🎯 Objetivo

Construir uma API REST simples com o framework FastAPI, praticando rotas, métodos HTTP, validação de dados com Pydantic e documentação automática.

## 📝 Tarefas

### 🛠️ Primeira Rota

#### Descrição
Crie uma aplicação FastAPI com uma rota de boas-vindas e uma rota de status. Antes de começar, instale as dependências com `pip install fastapi uvicorn`. Copie o starter code para um arquivo `main.py` e execute o servidor com `uvicorn main:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` chamada `app`.
- Responder a `GET /` com a mensagem `{"message": "Welcome to the API"}`.
- Responder a `GET /status` com `{"status": "ok"}`.

### 🛠️ Recursos com Caminho e Parâmetros

#### Descrição
Crie uma rota que retorne um item da lista de livros pelo seu identificador, usando um parâmetro de caminho.

#### Requisitos
O programa concluído deve:

- Manter uma lista de livros em memória, com `id`, `title` e `author`.
- Responder a `GET /books/{book_id}` com o livro correspondente.
- Retornar status `404` quando o livro não existir. Use `HTTPException` para isso.

### 🛠️ Criação de Dados com Validação

#### Descrição
Crie uma rota que adicione novos livros à lista. Use um modelo Pydantic para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `Book` com os campos `title` (texto) e `author` (texto).
- Responder a `POST /books` adicionando o livro à lista e retornando-o com um `id` gerado automaticamente.
- Retornar status `422` quando o corpo da requisição não tiver os campos obrigatórios. Isso acontece automaticamente com o FastAPI.

### 🛠️ Atualização e Remoção

#### Descrição
Complete o CRUD da API com rotas para atualizar e remover livros.

#### Requisitos
O programa concluído deve:

- Responder a `PUT /books/{book_id}` atualizando os dados do livro.
- Responder a `DELETE /books/{book_id}` removendo o livro da lista.
- Retornar status `404` nas duas rotas quando o livro não existir.

Depois de concluir, acesse `http://127.0.0.1:8000/docs` no navegador para testar sua API pela documentação interativa gerada pelo FastAPI.
