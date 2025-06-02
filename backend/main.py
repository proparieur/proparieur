from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fortuNePluS@2025")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///local.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Exemple route
@app.route('/')
def index():
    return "Bienvenue sur Fortune Plus !"

if __name__ == "__main__":
    app.run(debug=True)
