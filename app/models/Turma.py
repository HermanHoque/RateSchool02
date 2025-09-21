from app import db
from .BaseModel import CreateUpdate


class Turma(CreateUpdate):
    __tablename__ = 'turma'

    id_turma = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    ano_classe = db.Column(db.String(20), nullable=False)
    sala = db.Column(db.String(20), nullable=False)
    turno = db.Column(db.String(20), nullable=False)
    ano_lectivo = db.Column(db.String(20), nullable=False)
    limite_alunos = db.Column(db.Integer, nullable=False)

    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    id_escola = db.Column(db.Integer, db.ForeignKey('escola.id_escola'), nullable=False)

    curso = db.relationship('Curso', back_populates='turma')
    escola = db.relationship('Escola', back_populates='turma')
    aluno = db.relationship('Aluno', back_populates='turma')

    #relacionamento muitos para muitos
    disciplina = db.relationship(
        'Disciplina', 
        secondary='disciplina_turma', 
        back_populates='turma'
    )

    def to_dict(self):
        return {
            'id_turma': self.id_turma,
            'nome': self.nome,
            'ano_classe': self.ano_classe,
            'sala': self.sala,
            'turno': self.turno,
            'ano_lectivo': self.ano_lectivo,
            'limite_alunos': self.limite_alunos,
            'id_curso': self.id_curso,
            'id_escola': self.id_escola
        }

    