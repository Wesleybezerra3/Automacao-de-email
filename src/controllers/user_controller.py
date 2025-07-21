from sqlalchemy.orm import Session
from src.models.user_model import User
from src.config.db import SessionLocal  # sua instância do banco
from src.utils.hash import hash_password    # função que criamos acima
from src.utils.jwt import generate_token

import bcrypt

db: Session = SessionLocal()


def registerUser (user_data):
    name = user_data.name
    email = user_data.email
    password = user_data.password
    
    existing_user = db.query(User).filter_by(email=email).first()
    if existing_user:
        raise Exception("E-mail já cadastrado.")
    
    password_hash = hash_password(password)
    
    new_user = User(
        name = name,
        email = email,
        password = password_hash
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return("Usuário criado com sucesso!")

def loginUser(email, password):
    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise Exception("Usúario não existe")
    
    compare_password = bcrypt.checkpw(password.encode(), user.password.encode())
    if not compare_password:
        raise Exception("Senha incorreta!")
        
    token = generate_token(user.id)
    return {
        "data":{
         "token":token
        },
        "message":"Usúario logado com sucesso!"  
    }
    
        

