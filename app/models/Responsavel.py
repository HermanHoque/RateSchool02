from app import db
from .BaseModel import CreateUpdate


class Responsavel(CreateUpdate):
    __tablename__ = 'responsavel'

    id_responsavel = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    #chamada da chave estrangeira
    id_escola = db.Column(db.Integer, db.ForeignKey('escola.id_escola'), nullable=False)

    #definir relacionamento
    escola = db.relationship("Escola", back_populates="responsavel")
    formulario_avaliacao = db.relationship("Formulario_Avaliacao", back_populates="responsavel")


    def to_dict(self):
        return {
            'id': self.id_responsavel,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'senha': self.senha,
            'id_escola': self.id_escola
        }