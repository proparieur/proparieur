from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from models import Retrait
from app import db

retrait_bp = Blueprint('retrait', __name__)

@retrait_bp.route('/retrait', methods=['GET', 'POST'])
@login_required
def retrait():
    if request.method == 'POST':
        montant = int(request.form['montant'])
        retrait = Retrait(user_id=current_user.id, montant=montant, statut='en attente')
        db.session.add(retrait)
        db.session.commit()
        flash("Demande de retrait envoyée.", "info")
        return redirect(url_for('user.dashboard'))
    return render_template('retrait.html')
