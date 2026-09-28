from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from models.usuario import Usuario

def cadastrar():
    dados = request.json

    usuario = Usuario(
        nome=dados["nome"],
        email=dados["email"],
        senha=generate_password_hash(dados["senha"])
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso"}), 201

def login():
    dados = request.json
    usuario = Usuario.query.filter_by(email=dados["email"]).first()

    if not usuario or not check_password_hash(usuario.senha, dados["senha"]):
        return jsonify({"erro": "Email ou senha inválidos"}), 401

    token = create_access_token(identity=str(usuario.id))

    return jsonify({"token": token})

@jwt_required()
def buscar(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    })

@jwt_required()
def atualizar(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    dados = request.json
    usuario.nome = dados["nome"]
    usuario.email = dados["email"]

    if "senha" in dados:
        usuario.senha = generate_password_hash(dados["senha"])

    db.session.commit()

    return jsonify({"mensagem": "Usuário atualizado com sucesso"})

@jwt_required()
def excluir(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensagem": "Usuário excluído com sucesso"})