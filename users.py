from flask import abort, make_response
from config import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from models.User import User, users_schema, user_schema

#####################################################
#
# FUNCTIONS CALLED BY THE OPEN API ENDPOINTS
#
#####################################################

# read all user from de data base
def read_all():
    users = User.query.all()

    return users_schema.dump(users)


# read a specific user from de data base
def read_one(control_number):
    user = User.query.filter(User.control_number == control_number).one_or_none()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"User with control number {control_number} not found"
        )


# create a new user. the user parameter is an object provided by the API
def create(user):
    email = user.get("email")
    existing_user = User.query.filter(User.email == email).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user), 201
    else:
        abort(
            406, f"User with email {email} already exists"
        )


# User attributes that can be updated in the database
def update(email, user):
    existing_user = User.query.filter(User.control_number == email).one_or_none()

    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.names = update_user.names
        existing_user.surname = update_user.surname
        existing_user.password = update_user.password
        existing_user.datebirth = update_user.datebirth
        db.session.commit()

        return user_schema.dump(existing_user), 201
    
    else:
        abort(
            404, f"User with email {email} not found"
        )


def delete():
    pass

#######################################################
#
# CLASSES AND FUNCTIONS FOR LOGIN
#
#######################################################

class CheckLogin(UserMixin):
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
    

     # comprobación de password
    # password en la BBDD se guarda en formato hash
    @classmethod   # método de clase para evitar instanciar
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def gener_password_hash(password):
        print(generate_password_hash(password))


class UserLogin():
    
    @classmethod
    def login(self, user):
        try:
            exist_user = User.query.filter(User.email == user.email).one_or_none()
            if exist_user is not None:
                is_user = CheckLogin(exist_user.email, CheckLogin.check_password(exist_user.password, user.password))
                return is_user
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def get_user_by_email(email):
        try:
            exist_user = User.query.filter(User.email == email).one_or_none()

            if exist_user is not None:
                return CheckLogin(exist_user.email, None)
            else:
                return None
        except Exception as e:
            raise Exception(e)
