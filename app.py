from flask import Flask, jsonify

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

@app.route('/exercicios', methods=['GET'])

def get_exercicios():
    return jsonify({"exercicios": exercicios}), 200

if __name__ == "__main__":
    app.run(debug=True)