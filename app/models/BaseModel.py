from datetime import datetime
from app import db


class CreateUpdate(db.Model):
    __abstract__ = True  # Indica que esta é uma classe abstrata (não cria tabela)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)