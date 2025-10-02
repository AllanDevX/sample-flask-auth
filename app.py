from flask import Flask, requests, jsonify
from models.user import User
from database import db
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Criando variavel para receber a instância
login_manger = LoginManager()
db.init_app(app)
# Inicando o aplicativo
login_manger.init_app(app)

# view login

# Session <- conexão ativa

@app.route('/login', methods=["POST"])
def login():
    data = requests.json
    username = data.get("usename")
    password = data.get("password")

    if username and password:
        # Login
        pass
    return jsonify({"Message": "Credenciais Invalidas"}), 404
@app.route("/hello-world", methods=["GET"])
def hello_word():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)