from flask import Flask, jsonify, request
from validator import Validator
from db import exercicios, alunos
from flask_smorest import abort
import uuid
# Instanciando o flask
app = Flask(__name__)

'''exercicios = [
    {
        "id": 1,
        "nome": "supino reto",
        "grupo_muscular": "peito",
        "series": 4,
        "repeticoes": 12
    },
    {
        "id": 2,
        "nome": "puxada frontal",
        "grupo_muscular": "costas",
        "series": 3,
        "repeticoes": 12
    }
]'''

# rotas

# listar todas os exercicios
@app.route('/exercicios', methods=['GET'])
def get_exercicios():
    return jsonify({"exercicios": list(exercicios.values())}), 200



# buscar exercicio por id
@app.route('/exercicios/<string:id>', methods=['GET'])
def get_exercicios_by_id(id):
    try:
        return jsonify(exercicios[id]), 200
    except KeyError:
        return jsonify({"erro": "Exercicio não encontrado"}), 404
        #não esta funcionando o abort
        #abort(404, message="exercicio não encontrado.")

    


#busca do exercio por nome
@app.route('/exercicio', methods=['GET'])
def get_for_nome():
    nome = request.args['nome']
    
    for exercicio in exercicios.values():
        if exercicio['nome'] == nome:
            return jsonify({'exercicio': exercicio}), 200

    return jsonify({"erro": "Exercicio não encontrado"}), 404
    #não esta funcionando o abort
    #abort(404, message="exercicio não encontrado")  
    




#criar um exercicio
@app.route('/exercicio', methods=['POST'])
def create_exercicio():
    
    dado = request.get_json()
    exercicio_id = uuid.uuid4().hex

    erros = Validator.validar_post(dado)
    if erros:
        return jsonify({"erros": erros}), 400

    novo_exercicio = {**dado, "id":exercicio_id}
    exercicios[exercicio_id] = novo_exercicio


    return jsonify({"exercicio criado": novo_exercicio}), 201



#atualizar exercicios
@app.route('/exercicio/<string:id>', methods=['PUT'])
def update_exercicio(id):
    novo_dado = request.get_json()

    erros = Validator.validar_put_del(novo_dado)

    if erros:
        return jsonify({"erros": erros}), 400
    
    for exercicio in exercicios.values():
        if exercicio['id'] == id:

            exercicio.update(novo_dado)

            return jsonify({"exercicio atualizado": exercicio}), 200
        
    return jsonify({"erro": "Exercicio não encontrado"}), 404





#deletar um exercicio
@app.route('/exercicio/<string:id>', methods=['DELETE'])
def delete_exercicio(id):
    try:
        exercicios.pop(id)
    
        return jsonify({"mensagem": "exercicio removido com sucesso"}), 200
    except KeyError:
        return jsonify({"erro": "exercicio não encontrado"}),404
        #não esta funcionando o abort
        #abort(404, message="exercicio não encontrada.")




# listar todos os alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify({"alunos": list(alunos.values())}), 200



#cadastrar um aluno
@app.route('/aluno', methods=['POST'])
def cadastrar_aluno():
    
    dado = request.get_json()
    aluno_id = uuid.uuid4().hex

    novo_aluno = {**dado, "id":aluno_id}
    alunos[aluno_id] = novo_aluno


    return jsonify({"aluno criado": novo_aluno}), 201




#buscar aluno por id
@app.route('/alunos/<string:id>', methods=['GET'])
def get_aluno_by_id(id):
    try:
        aluno = alunos[id]
        return jsonify({"aluno": aluno}), 200
    except KeyError:
        return jsonify({"erro": "aluno não encontrado"}), 404
        #não esta funcionando o abort
        #abort(404, message="aluno não encontrado.")
        
    


#busca do aluno por nome
@app.route('/aluno', methods=['GET'])
def get_for_nome_aluno():

    nome = request.args.get('nome')
    
    for aluno in alunos.values():
        if aluno['nome'] == nome:
            return jsonify({'aluno': aluno}), 200

    return jsonify({"erro": "aluno não encontrado"}), 404




#atualizar alunos
@app.route('/aluno/<string:id>', methods=['PUT'])
def update_aluno(id):
    
    novo_dado = request.get_json()
    
    for aluno in alunos.values():
        if aluno['id'] == id:
            aluno.update(novo_dado)

            return jsonify({"aluno atualizado": aluno}), 200
        
    return jsonify({"erro": "aluno não encontrado"}), 404



#deletar um aluno
@app.route('/aluno/<string:id>', methods=['DELETE'])
def delete_aluno(id):
    try:
        alunos.pop(id)
    
        return jsonify({"mensagem": "aluno removido com sucesso"}), 200
    except KeyError:
        return jsonify({"erro": "aluno não encontrado"}), 404
        #não esta funcionando o abort
        #abort(404, message="aluno não encontrado.")





if __name__ == "__main__":
    app.run(debug=True)