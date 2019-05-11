from werkzeug.security import check_password_hash
from App.DB import *
from flask_jwt_extended import create_access_token, create_refresh_token


class AuthModel:

    @staticmethod
    def login(email, password):

        mysql = app.mysql
        cur = mysql.cursor()
        sql = '''SELECT email, password FROM user WHERE email = '{}';'''.format(email)
        cur.execute(sql)
        data = cur.fetchone()

        if data is None or not check_password_hash(data[1], password):
            return False

        response = {
            'access_token': create_access_token(identity=email),
            'refresh_token': create_refresh_token(identity=email)
        }
        return response
