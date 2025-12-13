from flask import Flask, jsonify, request

# Instanciando o flask
app = Flask(__name__)

exercicios = [
    {
        "id": 1,
        "nome": "supino reto",
        "grupo_muscular": "peito",
        "series": 4,
        "repetições": 12
    },
    {
        "id": 2,
        "nome": "puxada frontal",
        "grupo_muscular": "costas",
        "series": 3,
        "repetições": 12
    }
]

# rotas

# listar todas os exercicios
@app.route('/exercicios', methods=['GET'])
def get_exercicios():
    return jsonify({"exercicios": exercicios}), 200


#buscar exercicio por id
@app.route('/exercicios/<int:id>', methods=['GET'])
def get_exercicios_by_id(id):
    
    for exercicio in exercicios:
        if exercicio["id"] == id:
            return jsonify({"exercicio": exercicio}), 200
    
    return jsonify({"erro": "exercicio não encontrado"}), 404



#busca do exercio por nome
@app.route('/exercicio', methods=['GET'])
def get_for_nome():
    nome = request.args['nome']
    
    for exercicio in exercicios:
        if exercicio['nome'] == nome:
            return jsonify({'exercicio': exercicio}), 200
    
    return jsonify({"erro": "exercicio não encontrado"}),404




if __name__ == "__main__":
    app.run(debug=True)