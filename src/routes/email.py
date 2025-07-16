from flask import Blueprint, jsonify
from src.controllers.email_controller import processar_emails  # importa o controller

emailRouter = Blueprint('emails', __name__)

@emailRouter.route('/', methods=['GET'])
def ativar_automacao():
    data = processar_emails()
    return jsonify({"data":{"processados": f"{data["processados"]} e-mails processados", "emails": data["emails"]}})
    
    