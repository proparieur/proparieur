from flask_login import UserMixin
from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv
import uuid

# Chargement des variables d’environnement
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
MONTANT_COTATION = int(os.getenv("MONTANT_COTATION", 2000))
POURCENTAGE_REPARTITION = float(os.getenv("POURCENTAGE_REPARTITION", 0.10))
NOMBRE_FILLEULS_MAX = int(os.getenv("NOMBRE_FILLEULS_MAX", 4))

# Création du client Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Générateur d'UUID unique
def generate_id():
    return str(uuid.uuid4())

# === UTILISATEUR ===
class User(UserMixin):
    def __init__(self, id, nom, email, password, telephone,
                 parrain_id=None, inscrit_le=None, filleuls=None,
                 is_admin=False, a_jour=False):
        self.id = id
        self.nom = nom
        self.email = email
        self.password = password
        self.telephone = telephone
        self.parrain_id = parrain_id
        self.inscrit_le = inscrit_le or datetime.utcnow().isoformat()
        self.filleuls = filleuls or []
        self.is_admin = is_admin
        self.a_jour = a_jour

    def get_id(self):
        return self.id

    @staticmethod
    def get_by_id(user_id):
        res = supabase.table("users").select("*").eq("id", user_id).execute()
        if res.data:
            return User(**res.data[0])
        return None

    @staticmethod
    def get_by_email(email):
        res = supabase.table("users").select("*").eq("email", email).execute()
        if res.data:
            return User(**res.data[0])
        return None

    def save(self):
        data = self.__dict__.copy()
        data["inscrit_le"] = self.inscrit_le
        supabase.table("users").upsert(data).execute()

# === COTATION ===
class Cotation:
    def __init__(self, id, user_id, montant, date_paiement=None, mois=None, annee=None):
        self.id = id
        self.user_id = user_id
        self.montant = montant
        self.date_paiement = date_paiement or datetime.utcnow().isoformat()
        self.mois = mois or datetime.utcnow().month
        self.annee = annee or datetime.utcnow().year

    def save(self):
        supabase.table("cotations").upsert(self.__dict__).execute()

# === TRANSACTION ===
class Transaction:
    def __init__(self, id, user_id, type, montant, date_operation=None, statut="en attente"):
        self.id = id
        self.user_id = user_id
        self.type = type
        self.montant = montant
        self.date_operation = date_operation or datetime.utcnow().isoformat()
        self.statut = statut

    def save(self):
        supabase.table("transactions").upsert(self.__dict__).execute()

# === RETRAIT ===
class Retrait:
    def __init__(self, id, user_id, montant, statut="en attente", demande_le=None):
        self.id = id
        self.user_id = user_id
        self.montant = montant
        self.statut = statut
        self.demande_le = demande_le or datetime.utcnow().isoformat()

    def save(self):
        supabase.table("retraits").upsert(self.__dict__).execute()

# === ANNONCE ===
class Annonce:
    def __init__(self, id, titre, description, type, fichier=None, date_creation=None):
        self.id = id
        self.titre = titre
        self.description = description
        self.type = type
        self.fichier = fichier
        self.date_creation = date_creation or datetime.utcnow().isoformat()

    def save(self):
        supabase.table("annonces").upsert(self.__dict__).execute()

# === OBJECTIF ===
class Objectif:
    def __init__(self, id, titre, description, type, fichier=None, date_creation=None):
        self.id = id
        self.titre = titre
        self.description = description
        self.type = type
        self.fichier = fichier
        self.date_creation = date_creation or datetime.utcnow().isoformat()

    def save(self):
        supabase.table("objectifs").upsert(self.__dict__).execute()

# === SUREBET ===
class Surebet:
    def __init__(self, id, match, cote1, cote2, gain_possible,
                 bookmaker1, bookmaker2, date_publication=None):
        self.id = id
        self.match = match
        self.cote1 = cote1
        self.cote2 = cote2
        self.gain_possible = gain_possible
        self.bookmaker1 = bookmaker1
        self.bookmaker2 = bookmaker2
        self.date_publication = date_publication or datetime.utcnow().isoformat()

    def save(self):
        supabase.table("surebets").upsert(self.__dict__).execute()
