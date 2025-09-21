from app import db
from .BaseModel import CreateUpdate

class Curso(CreateUpdate):
    __tablename__ = 'curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)

    #definir relacionamento muitos para muitos
    disciplina = db.relationship(
        'Disciplina', 
        secondary='disciplina_curso', 
        back_populates='curso'
    )

    def __repr__(self):
        return f'<Curso {self.nome}>'