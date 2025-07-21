from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from src.models.schemas import UserCreate 
from src.controllers.user_controller import registerUser, loginUser

userRouter = Blueprint('users', __name__)

@userRouter.route('/', methods=['GET'])
def listar_usuarios():
    return jsonify({"mensagem": "Lista de usuários"})

@userRouter.route('/register', methods=['POST'])
def register():
    try:
        user_data = UserCreate(**request.get_json())
        
        
        data = registerUser(user_data)
        return jsonify({
            "status": "success",
            "message": data
        }), 200
    except ValidationError as ve:
        errors = [
            f"{err['loc'][0]}: {err['msg']}"
            for err in ve.errors()
        ]
        return jsonify({
            "status": "error",
            "message": "Erro de validação",
            "errors": errors
        }), 422

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro ao cadastrar usuário: {str(e)}"
        }), 500
    
@userRouter.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get("password")
        data = loginUser(email, password)
        return jsonify({
            "status": "success",
            "data":data["data"],
            "message": data["message"]
        }), 200
        
    except Exception as e:
         return jsonify({ 
            "status":"error",
            "message": f"Erro ao logar usúario: {e}"
        }), 500
    
