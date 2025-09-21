from app import db
from .BaseModel import CreateUpdate

disciplina_professor = db.Table('disciplina_professor',
    db.Column('id_disci', db.Integer, db.ForeignKey('disciplina.id_disci'), primary_key=True),
    db.Column('id_prof', db.Integer, db.ForeignKey('professor.id_prof'), primary_key=True)
)

disciplina_curso = db.Table('disciplina_curso',
    db.Column('id_disci', db.Integer, db.ForeignKey('disciplina.id_disci'), primary_key=True),
    db.Column('id_curso', db.Integer, db.ForeignKey('curso.id_curso'), primary_key=True)
)

disciplina_turma = db.Table('disciplina_turma',
    db.Column('id_disci', db.Integer, db.ForeignKey('disciplina.id_disci'), primary_key=True),
    db.Column('id_turma', db.Integer, db.ForeignKey('turma.id_turma'), primary_key=True)
)


class Disciplina(CreateUpdate):
    __tablename__ = 'disciplina'

    id_disci = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)

    #definir relacionamento muitos para muitos
    professore = db.relationship(
        'Professor', 
        secondary=disciplina_professor, 
        back_populates='disciplina'
    )

    curso = db.relationship(
        'Curso', 
        secondary=disciplina_curso, 
        back_populates='disciplina'
    )

    turma = db.relationship(
        'Turma', 
        secondary=disciplina_turma, 
        back_populates='disciplina'
    )


    def __repr__(self):
        return f'<Disciplina {self.nome}>'