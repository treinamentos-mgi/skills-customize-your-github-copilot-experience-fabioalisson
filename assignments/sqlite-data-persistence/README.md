# 📘 Atividade: Persistência de Dados com SQLite

## 🎯 Objetivo

Aprender a salvar e consultar dados usando SQLite e o módulo `sqlite3`, incluído no Python. Ao final, você terá um pequeno programa de cadastro de livros que mantém os dados mesmo depois de ser fechado.

## 📝 Tarefas

### 🛠️ Criar o Banco de Dados

#### Descrição
Complete a função `initialize_database()` no starter code. Ela deve criar o arquivo do banco de dados e uma tabela para armazenar livros.

#### Requisitos
O programa concluído deve:

- Usar o módulo `sqlite3`, sem instalar pacotes adicionais.
- Criar uma tabela `books` com `id`, `title` e `author`.
- Definir `id` como chave primária inteira gerada automaticamente.
- Poder executar a inicialização mais de uma vez sem falhar se a tabela já existir.

### 🛠️ Adicionar e Listar Livros

#### Descrição
Implemente as funções para adicionar um livro e listar os livros cadastrados.

#### Requisitos
O programa concluído deve:

- Salvar o título e o autor informados e deixar o banco gerar o identificador.
- Listar os livros com seus identificadores, títulos e autores.
- Usar parâmetros SQL (`?`) para passar valores às consultas.

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete as funções de atualização e remoção, usando o identificador para localizar cada livro.

#### Requisitos
O programa concluído deve:

- Atualizar o título e o autor do livro indicado.
- Remover o livro indicado sem afetar os outros registros.
- Informar se o identificador não foi encontrado.
- Verificar os resultados executando as operações e listando os livros após cada alteração.
