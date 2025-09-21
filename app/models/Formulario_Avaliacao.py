from app import db
from .BaseModel import CreateUpdate

class Formulario_Avaliacao(CreateUpdate):
    __tablename__ = 'formulario_avaliacao'

    id_form = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(40), nullable=False)

    for i in range(1, 21):
        vars()[f'topico{i}'] = db.Column(db.String(40), nullable=True)
    
    descricao = db.Column(db.String(40), nullable=True)

    id_responsavel = db.Column(db.Integer, db.ForeignKey('responsavel.id_responsavel'), nullable=False)

    #relações 
    responsavel = db.relationship("Responsavel", back_populates="formulario_avaliacao")
    avaliacao_prof = db.relationship("Avaliacao_Prof", back_populates="formulario_avaliacao")
    avaliacao_outros = db.relationship("Avaliacao_Outros", back_populates="formulario_avaliacao")
    


    def to_dict(self):
        data = {
            'id_form': self.id_form,
            'tipo': self.tipo,
            'descricao': self.descricao,
            'id_responsavel': self.id_responsavel,
        }
        for i in range(1, 21):
            data[f'topico{i}'] = getattr(self, f'topico{i}')
        return data