from flask import jsonify
from Model.Adm.UserModel import *


class UserController:

    @staticmethod
    def create(data):
        UserModel.create(data)
        return jsonify({'result': 'ok', 'data': []})
