from flask import Flask
from flask_wtf.csrf import CSRFProtect
from routes import pages_bp, errors_bp
from config import connex_app, base_dir

app = connex_app.app
connex_app.add_api(base_dir / 'api.yml')
csrf = CSRFProtect()

app.register_blueprint(pages_bp,  url_prefix='/')
app.register_blueprint(errors_bp, url_prefix='/')


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)