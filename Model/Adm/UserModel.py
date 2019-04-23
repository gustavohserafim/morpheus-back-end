from werkzeug.security import generate_password_hash, check_password_hash
import App
from App.DB import *

class UserModel:

    @staticmethod
    def create(data):
        DB.insert(data, 'user')
