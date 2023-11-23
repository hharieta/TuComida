import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import secrets
from envars import vars

# creates the variable basedir pointing 
# to the directory that the program is running in.
base_dir = pathlib.Path(__file__).parent.resolve()
# uses the basedir variable to create the Connexion app 
# instance and give it the path to the directory 
# that contains your specification file.
connex_app = connexion.App(__name__, specification_dir=base_dir)
connex_app.add_api(base_dir / 'api.yml')
# creates a variable, app,
# which is the Flask instance initialized by Connexion
app =connex_app.app


USERNAME = vars['POSTGRES_USERNAME']
PASSWORD = vars['POSTGRES_PASSWORD']
HOST = vars['POSTGRES_HOST']
PORT = vars['POSTGRES_PORT']
DBNAME = vars['POSTGRES_DBNAME']



# tell SQLAlchemy to use SQLite as the database
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

# turns the SQLAlchemy event system off. The event system 
# generates events that are useful in event-driven programs, 
# but it adds significant overhead. Since you’re not creating 
# an event-driven program, you turn this feature off.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Key secret for CSRF
app.config["SECRET_KEY"] = secrets.token_hex(32)

app.config['SESSION_TYPE'] = 'filesystem'

# initializes SQLAlchemy by passing the app 
# configuration information to SQLAlchemy 
# and assigning the result to a db variable.
db = SQLAlchemy(app)

# nitializes Marshmallow and allows it 
# to work with the SQLAlchemy components attached to the app.
ma = Marshmallow(app)
