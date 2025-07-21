from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DB_URL')

engine = create_engine(DB_URL)

# Teste de conexão
try:
    connection = engine.connect()
    print("Banco conectado com sucesso!")
    connection.close()
except Exception as e:
    print("Erro ao conectar:", e)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
