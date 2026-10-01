from flask_jwt_extended import jwt_required
from flask import jsonify, request
from db import db
from models.formulario import Formulario


@jwt_required()
def consultar_formulario(id):
    formulario = Formulario.query.get(id)

    if not formulario:
        return jsonify({"mensagem": "Formulário não encontrado"}), 404

    return jsonify({
        "id": formulario.id,
        "nome": formulario.nome,
        "email": formulario.email,
        "mensagem": formulario.mensagem
    }), 200


@jwt_required()
def atualizar_formulario(id):
    formulario = Formulario.query.get(id)

    if not formulario:
        return jsonify({"mensagem": "Formulário não encontrado"}), 404

    dados = request.get_json()

    formulario.nome = dados.get("nome", formulario.nome)
    formulario.email = dados.get("email", formulario.email)
    formulario.mensagem = dados.get("mensagem", formulario.mensagem)

    db.session.commit()

    return jsonify({
        "mensagem": "Formulário atualizado com sucesso"
    }), 200


@jwt_required()
def excluir_formulario(id):
    formulario = Formulario.query.get(id)

    if not formulario:
        return jsonify({"mensagem": "Formulário não encontrado"}), 404

    db.session.delete(formulario)
    db.session.commit()

    return jsonify({
        "mensagem": "Formulário excluído com sucesso"
    }), 200