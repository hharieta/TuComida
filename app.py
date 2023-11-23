from flask_wtf.csrf import CSRFProtect
from pages import pages_bp
from errors import errors_bp
from config import connex_app

app = connex_app.app
csrf = CSRFProtect(app)

app.register_blueprint(pages_bp,  url_prefix='/')
app.register_blueprint(errors_bp, url_prefix='/')


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)