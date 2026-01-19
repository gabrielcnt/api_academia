from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.exercicios import ExercicioSchema, ExercicioSchemaUpdate

from sqlalchemy.exc import SQLAlchemyError
from db import db

from models.exercicios import ExercicioModel

exercicio_bp = Blueprint("exercicio", __name__, description="operação relacionada exercicio")


@exercicio_bp.route('/exercicio')
class Exercicio(MethodView):
    
    @exercicio_bp.response(200, ExercicioSchema(many=True))
    def get(self):
        return ExercicioModel.query.all()

    
    @exercicio_bp.arguments(ExercicioSchema)
    @exercicio_bp.response(201, ExercicioSchema)
    def post(self, dado):

        novo_exercicio = ExercicioModel(**dado)
        try:
            db.session.add(novo_exercicio)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Erro: {str(e)}')
            abort(400, message="Erro ao criar exercicio: camos obrigatórios faltando")
        return novo_exercicio
    

@exercicio_bp.route('/exercicio/<string:id>')
class ExercicioId(MethodView):

    @exercicio_bp.response(200, ExercicioSchema)
    def get(self, id):
        exercicio = ExercicioModel.query.get(id)

        if not exercicio:
            abort(404, message="Exercicio não encontrado")
        
        return exercicio


    @exercicio_bp.arguments(ExercicioSchemaUpdate)
    @exercicio_bp.response(200, ExercicioSchema)
    def put(self, dado, id):

        exercicio = ExercicioModel.query.get(id)

        if not exercicio:
            abort(404, message="Exercicio não encontrado")
        
        exercicio.nome = dado["nome"]
        exercicio.grupo_muscular = dado["grupo_muscular"]
        exercicio.series = dado["series"]
        exercicio.repeticoes = dado["repeticoes"]

        try:
            db.session.add(exercicio)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Erro: {str(e)}')
            abort(400, message="Erro ao criar exercicio: campos obrigatórios faltando")
        
        return exercicio
    


    @exercicio_bp.arguments(ExercicioSchemaUpdate(partial=True))
    @exercicio_bp.response(200, ExercicioSchema)
    def patch(self, dado, id):
        exercicios = ExercicioModel.query.get(id)

        if not exercicios:
            abort(404, message="exercicio não encontrado")
    
        if "nome" in dado:
            exercicios.nome = dado["nome"]

        if "grupo_muscular" in dado:
            exercicios.grupo_muscular = dado["grupo_muscular"]
        
        if "series" in dado:
            exercicios.series = dado["series"]
        
        if "repeticoes" in dado:
            exercicios.repeticoes = dado["repeticoes"]

        try:
            db.session.add(exercicios)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Erro: {str(e)}')
            abort(400, message="Erro ao criar exercicio: campos obrigatórios faltando")

        return exercicios
        
    @exercicio_bp.response(200)
    def delete(self, id):
        exercicio = ExercicioModel.query.get(id)

        if not exercicio:
            abort(404, message="Exercicio não encontrado")

        db.session.delete(exercicio)
        db.session.commit()
        
        return jsonify({"mensagem": "exercicio removido com sucesso"}), 200
       