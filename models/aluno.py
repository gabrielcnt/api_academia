from db import db
from models.exercicios import ExercicioModel

class AlunoModel(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    nome = db.Column(db.String(90), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=True)

    exercicio = db.relationship("ExercicioModel", back_populates="aluno", cascade="all, delete-orphan")