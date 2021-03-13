
<h1 align="center">Simples Api service com flask</h1>

<p align="center">API desenvolvida para aprofundar o conhecimento sobre o microframework do ecossistema Python. Nela será possível fazer se inscrever, fazer login e gerenciar um post. Para saber mais detalhes do dados que são enviados e retornados clica <a href="https://documenter.getpostman.com/view/5841921/Tz5p4xBD#intro">aqui</a>.</p>

### Features

- [x] Cadastro do usuário
- [x] Login
- [x] Refresh Token 
- [x] Cadastro do post
- [x] Atualização do post
- [x] Remoção do post
- [x] Visualização de todos os posts
  
### 🛠 Tecnologias

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Python](https://www.python.org/)
  
### Como rodar a aplicação

- Fazer clone do projeto
  - git clone https://github.com/loressl/api_service_flask_python.git 
- Abre pasta do projeto
- Criar um arquivo .env e colocar
  - SECRET_KEY
  - SQLALCHEMY_DATABASE_URI = 'sqlite:/// <path do seu diretório>
- Criação de um ambiente 
  - python -m venv nome_venv 
- Ativação do ambiente
  - windows: nome_venv\Scripts\activate
  - Linux: source nome_venv/bin/activate
- Instalação das bibliotecas
  - pip install -r requirements.txt
- OBS: Sequência de comandos para utilizar o SQLITE
- Criação da pasta migrations
  - python run.py db init
- Migração e análise das tabelas
  - python run.py db migrate
- Atualiza o banco com as tabelas 
  - python run.py db upgrade 
- Rodar o servidor
  - python run.py runserver 
- Podem usar o Postman/Insomnia/Outros para testar

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
