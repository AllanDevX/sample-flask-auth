from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Criando variavel para receber a instância
login_manger = LoginManager()
db.init_app(app)
# Inicando o aplicativo
login_manger.init_app(app)

# view login
login_manger.login_view = 'login'
# Session <- conexão ativa


@login_manger.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:  
        # Login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"Message": "Autenticação realizada com sucesso"})
    
    return jsonify({"Message": "Credenciais Invalidas" }), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"Message": "Logout realizado com sucesso!"})

@app.route()

@app.route("/hello-world", methods=["GET"])
def hello_word():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)