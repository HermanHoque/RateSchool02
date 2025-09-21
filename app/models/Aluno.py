from app import db
from .BaseModel import CreateUpdate


class Aluno(CreateUpdate):
    __tablename__ = 'aluno'

    id_aluno = db.Column(db.Integer, primary_key=True)
    num_matricula = db.Column(db.String(20), nullable=False, unique=True)
    nome = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    senha = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(15), nullable=True)


    id_turma = db.Column(db.Integer, db.ForeignKey('turma.id_turma'), nullable=False)
    id_escola = db.Column(db.Integer, db.ForeignKey('escola.id_escola'), nullable=False)

    turma = db.relationship('Turma', back_populates='aluno')
    escola = db.relationship('Escola', back_populates='aluno')
    avaliacao_prof = db.relationship("Avaliacao_Prof", back_populates="aluno")
    avaliacao_outros = db.relationship("Avaliacao_Outros", back_populates="aluno")


    def to_dict(self):
        return {
            'id_aluno': self.id_aluno,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'id_turma': self.id_turma,
            'id_escola': self.id_escola
        }