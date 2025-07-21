from pydantic import BaseModel, EmailStr, constr, field_validator
import re

class UserCreate(BaseModel):
    name: constr(min_length=3, max_length=150)
    email: EmailStr
    password: str
    
    @field_validator('password')
    def validar_senha(cls, senha):
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        if not re.search(r"[A-Z]", senha):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r"[!@#$.]", senha):
            raise ValueError("A senha deve conter pelo menos um caractere especial (!@#$.).")
        return senha
