import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class Config:
    # === Flask Config ===
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24).hex())
    FLASK_APP = os.getenv("FLASK_APP", "main.py")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")  # pour Render : production
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "yes"]

    # === Supabase Config ===
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    # === PayDunya Config ===
    PAYDUNYA_API_KEY = os.getenv("PAYDUNYA_API_KEY")
    PAYDUNYA_PUBLIC_KEY = os.getenv("PAYDUNYA_PUBLIC_KEY")
    PAYDUNYA_PRIVATE_KEY = os.getenv("PAYDUNYA_PRIVATE_KEY")
    PAYDUNYA_MASTER_KEY = os.getenv("PAYDUNYA_MASTER_KEY")

    # === Paramètres métier ===
    MONTANT_COTATION = int(os.getenv("MONTANT_COTATION", 2000))
    NOMBRE_FILLEULS_MAX = int(os.getenv("NOMBRE_FILLEULS_MAX", 4))
    POURCENTAGE_REPARTITION = float(os.getenv("POURCENTAGE_REPARTITION", 0.10))

    # === Retraits ===
    RETRAIT_MIN = int(os.getenv("RETRAIT_MIN", 1000))
    RETRAIT_MAX = int(os.getenv("RETRAIT_MAX", 250000))
    RETRAIT_MAX_PAR_JOUR = int(os.getenv("RETRAIT_MAX_PAR_JOUR", 4))

    # === Admin Email ===
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@ozileudes.com")

    # === Noms des tables Supabase ===
    TABLE_USERS = os.getenv("TABLE_USERS", "users")
    TABLE_COTATIONS = os.getenv("TABLE_COTATIONS", "cotations")
    TABLE_TRANSACTIONS = os.getenv("TABLE_TRANSACTIONS", "transactions")
    TABLE_RETRAITS = os.getenv("TABLE_RETRAITS", "retraits")
    TABLE_ANNONCES = os.getenv("TABLE_ANNONCES", "annonces")
    TABLE_OBJECTIFS = os.getenv("TABLE_OBJECTIFS", "objectifs")
    TABLE_SUREBETS = os.getenv("TABLE_SUREBETS", "surebets")

    # === Pagination & sécurité ===
    ITEMS_PER_PAGE = int(os.getenv("ITEMS_PER_PAGE", 10))
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_DURATION = 60 * 60 * 24 * 30  # 30 jours
    SESSION_PROTECTION = "strong"

    # === Uploads autorisés ===
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_VIDEO_EXTENSIONS = {"mp4", "avi", "mov"}
    ALLOWED_TEXT_EXTENSIONS = {"txt", "pdf", "docx"}

    # === Upload folder (local ou Replit/Render) ===
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 Mo
