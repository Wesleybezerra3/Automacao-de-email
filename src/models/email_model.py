from sqlalchemy import Column, Integer, String, Text
from src.config.db import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    remetente = Column(String(255))
    assunto = Column(String(255))
    corpo = Column(Text)
    resposta = Column(Text)