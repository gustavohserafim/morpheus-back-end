from flask import jsonify
from Model.ClientModel import *


class ClientController:

    @staticmethod
    def all():
        return jsonify(ClientModel.all())

    @staticmethod
    def create(data):
        result = ClientModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
