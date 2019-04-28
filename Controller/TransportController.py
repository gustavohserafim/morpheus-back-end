from flask import jsonify
from Model.TransportModel import *


class TransportController:

    @staticmethod
    def all():
        return jsonify(TransportModel.all())

    @staticmethod
    def create(data):
        result = TransportModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
    @staticmethod
    def get(company_id):
        return jsonify({'result': 'ok', 'data': TransportModel.get(transport_id)}), 200

    @staticmethod
    def remove(company_id):
        TransportModel.remove(transport_id)
        return jsonify({'result': 'ok'}), 200
