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
