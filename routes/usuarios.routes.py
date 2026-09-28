from flask import Blueprint
from controllers.usuario_controller import cadastrar, login, buscar, atualizar, excluir

usuario_routes = Blueprint("usuario_routes", __name__)

usuario_routes.route("/usuarios", methods=["POST"])(cadastrar)
usuario_routes.route("/login", methods=["POST"])(login)
usuario_routes.route("/usuarios/<int:id>", methods=["GET"])(buscar)
usuario_routes.route("/usuarios/<int:id>", methods=["PUT"])(atualizar)
usuario_routes.route("/usuarios/<int:id>", methods=["DELETE"])(excluir)