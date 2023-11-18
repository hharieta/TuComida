from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__, template_folder='templates', static_folder='static')


@pages_bp.route('/')
def index():
    return render_template('index.html')

@pages_bp.route('/login')
def login():
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
