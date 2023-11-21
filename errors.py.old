from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__, template_folder='templates', static_folder='static')

@errors_bp.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404