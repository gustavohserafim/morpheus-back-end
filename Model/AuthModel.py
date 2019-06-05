from werkzeug.security import check_password_hash
from App.DB import DB
from flask_jwt_extended import create_access_token
from datetime import timedelta


class AuthModel:

    @staticmethod
    def login(email, password):
        db_password = DB().getPasswordByEmail(email)['password']
        if email is None or not check_password_hash(db_password, password):
            return False

        expires = timedelta(days=1)
        return create_access_token(identity=email, expires_delta=expires)

    @staticmethod
    def login_dev(email, password):
        db_password = DB().getPasswordByEmail(email)['password']
        if email is None or not check_password_hash(db_password, password):
            return False

        expires = timedelta(days=30)
        return create_access_token(identity=email, expires_delta=expires)
