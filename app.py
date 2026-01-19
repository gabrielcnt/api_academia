from flask import Flask, jsonify, request
from flask_smorest import Api

from db import db

from resource.exercicios import exercicio_bp
from resource.aluno import aluno_bp
# Instanciando o flask
def create_app(db_url=None):

    app = Flask(__name__)

    app.config["API_TITLE"] = "Api de academia"
    app.config["API_VERSION"] = "v1"
    app.config["PROPAGATE_EXCEPTIONS"] = True

    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)

    api.register_blueprint(exercicio_bp)
    api.register_blueprint(aluno_bp)

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)