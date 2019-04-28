from flask import jsonify
from Model.AddresModel import *


class AdressController:

    @staticmethod
    def all():
        return jsonify(AdressModel.all())

    @staticmethod
    def create(data):
        result = AdressModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})

    @staticmethod
    def get(id):
        return jsonify({'result': 'ok', 'data': AdressModel.get(id)}), 200

    @staticmethod
    def remove(id):
        AdressModel.remove(id)
        return jsonify({'result': 'ok'}), 200
