from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import alunos

import uuid

from schemas.aluno import AlunoSchema, AlunoSchemaUpdate

aluno_bp = Blueprint("aluno", __name__, description="operação relacionada alunos")


@aluno_bp.route('/alunos')
class Aluno(MethodView):

    @aluno_bp.response(200, AlunoSchema(many=True))
    def get(self):
        return jsonify({"alunos": list(alunos.values())}), 200
    


    @aluno_bp.arguments(AlunoSchema)
    @aluno_bp.response(201, AlunoSchema)
    def post(self, dado):

        aluno_id = uuid.uuid4().hex

        novo_aluno = {**dado, "id":aluno_id}
        alunos[aluno_id] = novo_aluno


        return jsonify({"aluno criado": novo_aluno}), 201



@aluno_bp.route('/alunos/<string:id>')
class AlunoId(MethodView):

    @aluno_bp.response(200, AlunoSchema)
    def get(self, id):
        try:
            aluno = alunos[id]
            return jsonify({"aluno": aluno}), 200
        except KeyError:
            abort(404, message="aluno não encontrado.")
            


    @aluno_bp.arguments(AlunoSchemaUpdate)
    @aluno_bp.response(200, AlunoSchema)
    def put(self, dado, id):

        for aluno in alunos.values():
            if aluno['id'] == id:
                aluno.update(dado)

                return jsonify({"aluno atualizado": aluno}), 200
            
        return jsonify({"erro": "aluno não encontrado"}), 404
    


    @aluno_bp.response(200)
    def delete(self, id):
        try:
            alunos.pop(id)
        
            return jsonify({"mensagem": "aluno removido com sucesso"}), 200
        except KeyError:
            abort(404, message="aluno não encontrado.")
