from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Cotation, User
from datetime import datetime
from app import db

cotation_bp = Blueprint('cotation', __name__)

@cotation_bp.route('/payer_cotation')
@login_required
def payer_cotation():
    montant = int(os.getenv("MONTANT_COTATION", 2000))
    cotation = Cotation(user_id=current_user.id, montant=montant, date=datetime.utcnow())
    db.session.add(cotation)
    db.session.commit()
    flash("Cotation payée avec succès.", "success")
    return redirect(url_for('user.dashboard'))
