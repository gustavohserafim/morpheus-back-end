from flask import jsonify
from Model.AdressModel import *


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
