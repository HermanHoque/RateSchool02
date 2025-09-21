from app import db
from .BaseModel import CreateUpdate


class Avaliacao_Outros(CreateUpdate):
    __tablename__ = 'avaliacao_outros'

    id_av = db.Column(db.Integer, primary_key=True)
    
    for i in range(1, 21):
        vars()[f'nota_topico{i}'] = db.Column(db.Integer, nullable=True)
    
    comentario = db.Column(db.String(100), nullable=True)

    id_form = db.Column(db.Integer, db.ForeignKey('formulario_avaliacao.id_form'), nullable=False)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id_aluno'), nullable=False)

    formulario_avaliacao = db.relationship("Formulario_Avaliacao", back_populates="avaliacao_outros")
    aluno = db.relationship("Aluno", back_populates="avaliacao_outros")

    def to_dict(self):
        data = {
            'id_av': self.id_av,
            'comentario': self.comentario,
            'id_form': self.id_form,
            'id_aluno': self.id_aluno,
        }
        for i in range(1, 21):
            data[f'nota_topico{i}'] = getattr(self, f'nota_topico{i}')
        return data