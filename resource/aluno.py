from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.aluno import AlunoSchema, AlunoSchemaUpdate
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.aluno import AlunoModel

aluno_bp = Blueprint("aluno", __name__, description="operação relacionada alunos")


@aluno_bp.route('/alunos')
class Aluno(MethodView):

    @aluno_bp.response(200, AlunoSchema(many=True))
    def get(self):
        return AlunoModel.query.all()
    


    @aluno_bp.arguments(AlunoSchema)
    @aluno_bp.response(201, AlunoSchema)
    def post(self, dado):

        novo_aluno = AlunoModel(**dado)
        try:
            db.session.add(novo_aluno)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Erro: {str(e)}')
            abort(400, message="Erro ao criar aluno: camos obrigatórios faltando")

        return novo_aluno




@aluno_bp.route('/alunos/<string:id>')
class AlunoId(MethodView):

    @aluno_bp.response(200, AlunoSchema)
    def get(self, id):
        aluno = AlunoModel.query.get(id)

        if not aluno:
            abort(404, message="Aluno não encontrado")

        return aluno


    @aluno_bp.arguments(AlunoSchemaUpdate)
    @aluno_bp.response(200, AlunoSchema)
    def put(self, dado, id):
        aluno = AlunoModel.query.get(id)

        if not aluno:
            abort(404, message="Aluno não encontrado")
        
        aluno.nome = dado["nome"]
        aluno.idade = dado["idade"]
        aluno.cpf = dado["cpf"]

        try:
            db.session.add(aluno)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Todos os campos são obrigatórios")
        
        return aluno
    


    @aluno_bp.response(200)
    def delete(self, id):
        aluno = AlunoModel.query.get(id)

        if not aluno:
            abort(404, message="Aluno não encontrado")

        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno removido com sucesso'})
