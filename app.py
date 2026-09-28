from flask import Flask
from flask_jwt_extended import JWTManager
from db import db
from routes.usuario_routes import usuario_routes

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/banco.db"
app.config["JWT_SECRET_KEY"] = "chave-secreta"

db.init_app(app)
JWTManager(app)

app.register_blueprint(usuario_routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)