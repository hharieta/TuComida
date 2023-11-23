from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, login_user, logout_user, login_required
from models import User
from config import connex_app
from services import CheckLogin, UserLogin
import logging

pages_bp = Blueprint('pages', __name__, template_folder='templates', static_folder='static')


login_manager = LoginManager(connex_app.app)

@login_manager.user_loader
def load_user(email):
    return UserLogin.get_user_by_email(email)

@pages_bp.route('/')
def index():
    return render_template('index.html')

@pages_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = CheckLogin(request.form['email'], request.form['password'])
        logged_user = UserLogin.login(user)

        if logged_user:
            login_user(logged_user)
            return redirect(url_for('pages.index'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('pages.login'))
    else:
        return render_template('login.html')

@pages_bp.route('/register')
def register():
    return render_template('register.html')

@pages_bp.route('/menus')
def menus():
    return render_template('menus.html')

@pages_bp.route('/resturant')
def restaurant():
    return render_template('restaurant.html')

@pages_bp.route('/faq')
def faq():
    return render_template('faq.html')

@pages_bp.route('/blog')
def blog():
    return render_template('blog.html')

@pages_bp.route('/contac')
def contac():
    return render_template('contac.html')

@pages_bp.route('/about')
def about():
    return render_template('about.html')

@pages_bp.route('/filos')
def filos():
    return render_template('filos.html')

@pages_bp.route('/registro')
def registro():
    return render_template('registro.html')

@pages_bp.route('/40x')
def err_404(error):
    return render_template('40x.html')
