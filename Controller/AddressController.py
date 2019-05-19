from flask import jsonify
from Model.AddressModel import *


class AddressController:

    @staticmethod
    def all():
        return jsonify(AddressModel.all())

    @staticmethod
    def create(data):
        result = AddressModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})

    @staticmethod
    def get(id):
        return jsonify({'result': 'ok', 'data': AddressModel.get(id)}), 200

    @staticmethod
    def remove(id):
        AddressModel.remove(id)
        return jsonify({'result': 'ok'}), 200
