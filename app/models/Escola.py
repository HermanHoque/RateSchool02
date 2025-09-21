from app import db
from .BaseModel import CreateUpdate


class Escola(CreateUpdate):
    __tablename__ = 'escola'

    id_escola = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    endereco = db.Column(db.String(40), nullable=False)

    Responsavel = db.relationship("Responsavel", back_populates="escola")
    turma = db.relationship("Turma", back_populates="escola")
    professor = db.relationship("Professor", back_populates="escola")
    aluno = db.relationship("Aluno", back_populates="escola")


    def to_dict(self):
        return {
            'id_escola': self.id_escola,
            'nome': self.nome,
            'email': self.email,
            'endereco': self.endereco
        }