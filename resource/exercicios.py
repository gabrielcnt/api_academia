from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import exercicios

import uuid

from validator import Validator

from schemas.exercicios import ExercicioSchema, ExercicioSchemaUpdate


exercicio_bp = Blueprint("exercicio", __name__, description="operação relacionada exercicio")


@exercicio_bp.route('/exercicio')
class Exercicio(MethodView):
    
    @exercicio_bp.response(200, ExercicioSchema(many=True))
    def get(self):
        return jsonify({"exercicios": list(exercicios.values())}), 200

    
    @exercicio_bp.arguments(ExercicioSchema)
    @exercicio_bp.response(201, ExercicioSchema)
    def post(self, dado):

        exercicio_id = uuid.uuid4().hex

        erros = Validator.validar_post(dado)
        if erros:
            return jsonify({"erros": erros}), 400

        novo_exercicio = {**dado, "id":exercicio_id}
        exercicios[exercicio_id] = novo_exercicio


        return jsonify({"exercicio criado": novo_exercicio}), 201




@exercicio_bp.route('/exercicio/<string:id>')
class ExercicioId(MethodView):

    @exercicio_bp.response(200, ExercicioSchema)
    def get(self, id):
        if id not in exercicios:
            return jsonify({"erro": "Exercicio não encontrado"}), 404

        try:
            return jsonify(exercicios[id]), 200
        except KeyError:   
            abort(404, message="exercicio não encontrado.")


    @exercicio_bp.arguments(ExercicioSchemaUpdate)
    @exercicio_bp.response(200, ExercicioSchema)
    def put(self, dado, id):

        if id not in exercicios:
            abort(404, message="Exercicio não encontrado")

        erros = Validator.validar_put_del(dado)

        if erros:
            return jsonify({"erros": erros}), 400
    
        for exercicio in exercicios.values():
            if exercicio['id'] == id:

                exercicio.update(dado)

                return jsonify({"exercicio atualizado": exercicio}), 200
        
        return jsonify({"erro": "Exercicio não encontrado"}), 404


    @exercicio_bp.arguments(ExercicioSchemaUpdate(partial=True))
    @exercicio_bp.response(200, ExercicioSchema)
    def patch(self, dado, id):

        if id not in exercicios:
            abort(404, message="exercicio não encontrado")
    

        if not dado or len(dado) == 0:
            abort(400, message="dado inválido, nenhum campo atualizado")
        
        if "id" in dado:
            if dado["id"] != id:
                abort(400, message="não é permitido alterar o id do exercicio")

        campos_permitidos = {"nome", "grupo_muscular", "series", "repeticoes"}

        campos_enviados = set(dado.keys())
        
        campos = campos_enviados - campos_permitidos

        if campos:
            abort(400, message="campos invalidos")
        
        exercicios[id].update(dado)

        return jsonify({"exercicio atualizado": exercicios}), 200


    @exercicio_bp.response(200)
    def delete(self, id):
        if id not in exercicios:
            abort(404, message="Exercicio não encontrado")

        try:
            exercicios.pop(id)
        
            return jsonify({"mensagem": "exercicio removido com sucesso"}), 200
        except KeyError:
            abort(404, message="exercicio não encontrada.")