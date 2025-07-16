from flask import Flask
from src.routes.user import userRouter
from src.routes.email import emailRouter


app = Flask(__name__)

app.register_blueprint(userRouter, url_prefix='/users')
app.register_blueprint(emailRouter, url_prefix='/emails')

app.run(port=5000, host='localhost',debug=True)