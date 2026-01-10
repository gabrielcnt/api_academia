from flask import Flask, jsonify, request
from validator import Validator
from flask_smorest import Api

from resource.exercicios import exercicio_bp
from resource.aluno import aluno_bp
# Instanciando o flask
app = Flask(__name__)

app.config["API_TITLE"] = "Api de academia"
app.config["API_VERSION"] = "v1"
app.config["PROPAGATE_EXCEPTIONS"] = True

app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(exercicio_bp)
api.register_blueprint(aluno_bp)



if __name__ == "__main__":
    app.run(debug=True)