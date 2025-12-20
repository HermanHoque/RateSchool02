# RateSchool

***APP feita com Python+Flask***
Sistema para avalição geral e personalizada para instituições escolares

Para rodar o projeto instale o python caso não tenha
e segue os passos no terminal dentro do diretório do projeto:

1- cria um ambiente virtual "python3 -m venv venv" ou "python -m venv venv"

2- entra no ambiente virtual criado: windows ->"venv\Scripts\activate" ou linux ->"source venv/bin/activate"

3- instale as bibliotecas no arquivo requirements.txt usando o seguinte comando no diretório do projeto: 
" pip install -r requirements.txt " 

4- renomeia o aquivo ".env.example" para ".env"

# Base de dados 

Para criar a base de dados usa os seguintes comandos no terminal do projecto

1-  flask db upgrade

# OBS: iniciar o projeto flask "flask run --debug"


# -----------------------------------------------------------------------


# 📌 FLASK-MIGRATE - COMANDOS MAIS USADOS

# 1) Inicializar migrations (apenas 1 vez no projeto)
flask db init

# 2) Criar um novo arquivo de migration (detecta mudanças nos models)
flask db migrate -m "descrição da alteração"
# Exemplo:
# flask db migrate -m "criação das tabelas aluno e professor"

# 3) Aplicar as migrations no banco de dados
flask db upgrade

# 4) Reverter (voltar) a uma versão anterior
flask db downgrade         # volta uma versão
flask db downgrade -1      # volta 1 migration
flask db downgrade -2      # volta 2 migrations

# 5) Mostrar a versão atual do banco
flask db current

# 6) Mostrar todas as migrations aplicadas e pendentes
flask db history

# 7) Mostrar a última migration (cabeça)
flask db heads

# 8) Criar tabelas diretamente dos models (não recomendado em produção)
# Use apenas no início do projeto ou para testes rápidos
flask shell
>>> from app import db, create_app
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()



