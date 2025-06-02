from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20), nullable=True)
    date_inscription = db.Column(db.DateTime, default=datetime.utcnow)
    est_actif = db.Column(db.Boolean, default=True)

    parrain_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    filleuls = db.relationship('User', backref=db.backref('parrain', remote_side=[id]), lazy=True)

    lien_parrainage = db.Column(db.String(255), unique=True)

    cotations = db.relationship('Cotation', backref='utilisateur', lazy=True)
    transactions = db.relationship('Transaction', backref='utilisateur', lazy=True)

    def est_a_jour(self):
        maintenant = datetime.utcnow()
        return any(c.date.month == maintenant.month and c.date.year == maintenant.year for c in self.cotations)

class Cotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    montant = db.Column(db.Integer, nullable=False, default=2000)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))  # 'depot' ou 'retrait'
    montant = db.Column(db.Integer, nullable=False)
    statut = db.Column(db.String(20), default='en_attente')  # 'en_attente', 'approuvé', 'refusé'
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Annonce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    type_contenu = db.Column(db.String(20), default='texte')  # 'texte', 'image', 'video'
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)

class Objectif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    type_contenu = db.Column(db.String(20), default='texte')  # 'texte', 'image', 'video'
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)

class Formation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    type_contenu = db.Column(db.String(20), default='texte')  # 'texte', 'image', 'video'
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)

class Surbet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match = db.Column(db.String(200), nullable=False)
    gain_potentiel = db.Column(db.Float, nullable=False)
    date_suggestion = db.Column(db.DateTime, default=datetime.utcnow)

class Filleul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    niveau = db.Column(db.Integer)  # de 1 à 6
    parrain_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    filleul_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_ajout = db.Column(db.DateTime, default=datetime.utcnow)

    parrain = db.relationship('User', foreign_keys=[parrain_id], backref='liens_filleuls')
    filleul = db.relationship('User', foreign_keys=[filleul_id])
