from werkzeug.security import generate_password_hash
from App.DB import *


class UserModel:

    @staticmethod
    def create(data):
        data['password'] = generate_password_hash(data['password'])
        DB().insert(data, 'user')
