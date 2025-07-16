from src.models.email_service import EmailService
from src.models.email_model import Email
from src.config.db import SessionLocal


email_service = EmailService()

def processar_emails():
    emails = email_service.ler_emails()
    email_obj = {
        "processados": 0,
        "emails": []
    }
    processados = 0


    for e in emails:
        resposta = "Obrigado por seu email. Estamos processando sua solicitação."
        email_service.enviar_email(e["from"], resposta)
        
        email_obj["emails"].append({
            "remetente": e["from"],
            "assunto": e["subject"],
            "corpo": e["body"],
            "resposta": resposta
         })

        email_obj["processados"] += 1
        
        

    print(f"✅ {processados} e-mails processados e salvos no banco.")
    return email_obj
 
