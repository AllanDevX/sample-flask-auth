from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Criando variavel para se conectar ao banco de dados
db = SQLAlchemy(app)
# Session <- conexão ativa

@app.route("/hello-world", methods=["GET"])
def hello_word():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)