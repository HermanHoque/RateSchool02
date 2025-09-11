import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "chave_padrao")
    
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL", "mysql+pymysql://root:''@127.0.0.1:3306/tutorlink")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False