from app import db
from .BaseModel import CreateUpdate


class Professor(CreateUpdate):
    __tablename__ = 'professor'

    id_prof = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)

    #chamada da chave estrangeira
    id_escola = db.Column(db.Integer, db.ForeignKey('escola.id_escola'), nullable=False)

    #definir relacionamento um para muitos
    escola = db.relationship("Escola", back_populates="professor")
    avaliacao_prof = db.relationship("Avaliacao_Prof", back_populates="professor")

    #definir relacionamento muitos para muitos
    disciplina = db.relationship(
        'Disciplina', 
        secondary='disciplina_professor', 
        back_populates='professor'
    )


    def to_dict(self):
        return {
            'id_prof': self.id_prof,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'senha': self.senha,
            'id_escola': self.id_escola
        }