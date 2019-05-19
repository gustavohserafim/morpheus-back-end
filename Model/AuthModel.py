from werkzeug.security import check_password_hash
from App.DB import DB
from flask_jwt_extended import create_access_token, create_refresh_token


class AuthModel:

    @staticmethod
    def login(email, password):
        db_password = DB().getPasswordByEmail(email)['password']
        if email is None or not check_password_hash(db_password, password):
            return False

        response = {
            'access_token': create_access_token(identity=email),
            'refresh_token': create_refresh_token(identity=email)
        }
        return response
