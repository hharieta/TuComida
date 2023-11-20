from marshmallow_sqlalchemy import fields
from ..config import db, ma

class User(db.Model):
    __tablename__ = "users"
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    names = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32), nullable=False)
    datebirth = db.Column(db.String(32))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sql_session = db.session

user_schema = UserSchema()
# parameter many=True tells to UserSchema
# to expect an iterable to serialize
users_schema = UserSchema(many=True)