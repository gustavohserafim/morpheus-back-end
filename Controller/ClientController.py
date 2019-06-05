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
            return jsonify({'error': True, 'message': 'failed to insert'}), 400
        return jsonify({'result': 'ok'}), 200

    @staticmethod
    def get(client_id):
        client = ClientModel.get(client_id)
        if len(client) < 1:
            return jsonify({"result": "not found"}), 404
        return jsonify({'result': 'ok', 'data': client}), 200

    @staticmethod
    def update(client_id, params):
        update = ClientModel.update(client_id, params)
        if update is False:
            return jsonify({'error': True, 'message': 'failed to update'}), 400
        return jsonify({'result': 'ok'}), 200

    @staticmethod
    def remove(client_id):
        ClientModel.remove(client_id)
        return jsonify({'result': 'ok'}), 200
