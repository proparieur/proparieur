from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import User

filleul_bp = Blueprint('filleul', __name__)

@filleul_bp.route('/mes_filleuls')
@login_required
def mes_filleuls():
    filleuls = User.query.filter_by(parrain_id=current_user.id).all()
    return render_template('filleuls.html', filleuls=filleuls)
