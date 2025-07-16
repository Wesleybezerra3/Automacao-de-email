from flask import Blueprint, jsonify

userRouter = Blueprint('users', __name__)

@userRouter.route('/', methods=['GET'])
def listar_usuarios():
    return jsonify({"mensagem": "Lista de usuários"})