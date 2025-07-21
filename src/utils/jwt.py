import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

SECRET_KEY = secret_key

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2) 
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
