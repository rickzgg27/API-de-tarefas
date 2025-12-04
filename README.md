🚀 API de Tarefas (Node.js + Express + SQLite)

Uma API REST simples para gerenciamento de tarefas.
Criada com foco em estudos de backend, rotas HTTP, banco de dados SQLite e estruturação clara de um servidor Node.js.

📌 Funcionalidades

✔ Listagem de tarefas

✔ Criação de tarefas

✔ Banco SQLite integrado

✔ API pronta para ser consumida por front-end (React, mobile, etc.)

🛠 Tecnologias Utilizadas

Node.js

Express

SQLite

ESModules

NPM

📁 Estrutura do Projeto
/
├── index.js
├── tasks.db
└── package.json

🔗 Endpoints
GET /tasks

Retorna todas as tarefas cadastradas.

Resposta:

[
  { "id": 1, "title": "Estudar Node" },
  { "id": 2, "title": "Criar API" }
]

POST /tasks

Cria uma nova tarefa.

Body JSON:

{
  "title": "Minha nova tarefa"
}


Resposta:

{
  "message": "Tarefa criada!"
}

▶ Como Rodar o Projeto
1️⃣ Instalar dependências
npm install

2️⃣ Executar a API
node index.js


A API estará rodando em:
👉 http://localhost:3000

🧪 Testar com Insomnia, Postman ou Thunder Client
Testar GET:

Método: GET

URL: http://localhost:3000/tasks

Testar POST:

Método: POST

URL: http://localhost:3000/tasks

Body: JSON

{ "title": "Nova tarefa" }

🎯 Objetivo do Projeto

Este projeto foi criado para treinar:

Roteamento com Express

Integração com SQLite

Métodos HTTP (GET/POST)

Organização de API simples

Node.js com ESModules

👨‍💻 Autor

João Victor Sena
Desenvolvedor Fullstack | React & Node.js
