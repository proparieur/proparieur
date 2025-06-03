import os
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client, Client

# === Chargement des variables d'environnement ===
load_dotenv()

# === Initialisation de l'app Flask ===
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

# === CORS (autorise les requêtes multi-origines, ex. frontend GitHub Pages) ===
CORS(app)

# === Configuration de Flask-Mail ===
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('ADMIN_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # mail pass séparé du SECRET_KEY

mail = Mail(app)

# === Configuration Supabase ===
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# === Authentification Flask-Login ===
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# === Chargement du modèle User ===
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)  # Assure-toi que cette méthode existe dans ton modèle

# === Importation des Blueprints ===
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.admin_routes import admin_bp
from routes.cotations_routes import cotations_bp
from routes.transactions_routes import transactions_bp
from routes.withdrawal_routes import withdrawal_bp
from routes.referral_routes import referral_bp
from routes.surebet_routes import surebet_bp
from routes.payment_routes import payment_bp
from routes.misc_routes import misc_bp

# === Enregistrement des Blueprints avec leurs préfixes ===
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(cotations_bp, url_prefix="/cotations")
app.register_blueprint(transactions_bp, url_prefix="/transactions")
app.register_blueprint(withdrawal_bp, url_prefix="/withdrawal")
app.register_blueprint(referral_bp, url_prefix="/referrals")
app.register_blueprint(surebet_bp, url_prefix="/surebets")
app.register_blueprint(payment_bp, url_prefix="/payment")
app.register_blueprint(misc_bp, url_prefix="/misc")

# === Route d'accueil ===
@app.route('/')
def home():
    return "Bienvenue sur la plateforme LA FORTUNE S’IMPOSE À NOUS !"

# === Lancement local uniquement ===
if __name__ == '__main__':
    if os.getenv("FLASK_ENV") == "development":
        app.run(debug=True)
