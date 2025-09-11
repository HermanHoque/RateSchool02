from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

     # Usa a configuração de desenvolviment no arquivo config.py
    app.config.from_object(DevelopmentConfig)

    # Inicializa o banco de dados e migrações
    db.init_app(app)
    migrate.init_app(app, db)

    # Importa e registra rotas
    from .routes.ola_mundo import ola
    app.register_blueprint(ola)

    return app


def get_connection():
    import pymysql

    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="tutorlink",
        cursorclass=pymysql.cursors.DictCursor  # retorna resultados como dicionário
    )
