from flask import jsonify
from Model.Ci_itemModel import *


class Ci_itemController:

    @staticmethod
    def all():
        return jsonify(Ci_itemModel.all())

    @staticmethod
    def create(data):
        result = Ci_itemModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok'}), 200

    @staticmethod
    def get(client_id):
        return jsonify({'result': 'ok', 'data': Ci_itemModel.get(client_id)}), 200

    @staticmethod
    def remove(client_id):
        Ci_itemModel.remove(client_id)
        return jsonify({'result': 'ok'}), 200
