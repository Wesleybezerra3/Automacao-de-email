import imaplib
import smtplib
import email
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"

class EmailService:
    def ler_emails(self):
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, SENHA)
        mail.select("inbox")

        status, mensagens = mail.search(None, 'UNSEEN')
        emails = []

        for num in mensagens[0].split():
            _, dados = mail.fetch(num, "(RFC822)")
            if dados and dados[0]:
                mensagem = email.message_from_bytes(dados[0][1])
                assunto = mensagem["subject"]
                remetente = mensagem["from"]
                corpo = ""

                if mensagem.is_multipart():
                    for parte in mensagem.walk():
                        if parte.get_content_type() == "text/plain":
                            corpo += parte.get_payload(decode=True).decode()
                else:
                    corpo = mensagem.get_payload(decode=True).decode()

                emails.append({"from": remetente, "subject": assunto, "body": corpo})

        mail.logout()
        return emails

    def enviar_email(self, destinatario, corpo):
        msg = MIMEText(corpo)
        msg["Subject"] = "Resposta automática"
        msg["From"] = EMAIL
        msg["To"] = destinatario

        with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
            server.login(EMAIL, SENHA)
            server.send_message(msg)
