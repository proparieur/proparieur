from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

depot_bp = Blueprint('depot', __name__)

@depot_bp.route('/depot')
@login_required
def depot():
    # À compléter avec PayDunya ou CinetPay
    return render_template('depot.html')
