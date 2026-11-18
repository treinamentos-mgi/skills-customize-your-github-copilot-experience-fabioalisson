from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Lista de livros em memória
books = [
    {"id": 1, "title": "Dom Casmurro", "author": "Machado de Assis"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]


class Book(BaseModel):
    title: str
    author: str


# Tarefa 1: crie as rotas GET / e GET /status


# Tarefa 2: crie a rota GET /books/{book_id}


# Tarefa 3: crie a rota POST /books


# Tarefa 4: crie as rotas PUT /books/{book_id} e DELETE /books/{book_id}
