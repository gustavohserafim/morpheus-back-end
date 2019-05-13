from flask import jsonify
from Model.ClientModel import *


class ClientController:

    @staticmethod
    def all():
        return jsonify({'data': ClientModel.all()})

    @staticmethod
    def create(data):
        result = ClientModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})


    @staticmethod
    def get(client_id):
        return jsonify({'result': 'ok', 'data': CompanyModel.get(client_id)}), 200

    @staticmethod
    def remove(client_id):
        ClientModel.remove(client_id)
        return jsonify({'result': 'ok'}), 200
