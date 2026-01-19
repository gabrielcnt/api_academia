from db import db

class ExercicioModel(db.Model):
    __tablename__ = 'exercicios'


    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    nome = db.Column(db.String(80), nullable=True)
    grupo_muscular = db.Column(db.String(100), nullable=False)
    series = db.Column(db.Integer, nullable=False)
    repeticoes = db.Column(db.Integer, nullable=False)
    
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id", ondelete="CASCADE"),nullable=False)
    
    aluno = db.relationship("AlunoModel", back_populates="exercicio")