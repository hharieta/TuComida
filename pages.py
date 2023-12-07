from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, login_user, logout_user, login_required
from models import User
from config import connex_app
from services import CheckLogin, UserLogin, UserRegister
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

        if logged_user is not None:
            login_user(logged_user) 
            flash("Login successful")
            return redirect(url_for('pages.homeuser'))
        else:
            flash("Invalid email or password")
            return render_template('login.html')

    return render_template('login.html')

@pages_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        names = request.form['names']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        surname = request.form['surname']
        datebirth = request.form['datebirth']
        terms = request.form['terms']

        if UserRegister.validate_email(email) is False:
            flash("User already exists")
            return render_template('register.html')
        if UserRegister.validate_password(password, confirm_password) is None:
            flash("Passwords do not match")
            return  render_template('register.html')
        if UserRegister.validate_terms(terms) is None:
            flash("You must accept the terms and conditions")
            return  render_template('register.html')
        
        user_signed = UserRegister.register(email, password, names, surname, datebirth)

        if user_signed:
            return redirect(url_for('pages.login'))
        else:
            return  render_template('register.html')
        
    else:
        return render_template('register.html')
    

@pages_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@pages_bp.route('/homeuser')
@login_required
def homeuser():
    return render_template('homeuser.html')

# @pages_bp.route('/register')
# def register():
#     return render_template('register.html')

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

@pages_bp.route('/ofertas')
def ofertas():
    return render_template('ofertas.html')

@pages_bp.route('/registro')
def registro():
    return render_template('registro.html')

@pages_bp.route('/400')
def err_404(error):
    return render_template('404.html')

@pages_bp.route('/plato')
def plato():
    return render_template('plato.html')

@pages_bp.route('/restaurant13')
def restaurant13():
    return render_template('restaurant13.html')