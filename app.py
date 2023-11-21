from flask import Flask
from routes import pages_bp, errors_bp

app = Flask(__name__)
app.register_blueprint(pages_bp,  url_prefix='/')
app.register_blueprint(errors_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)