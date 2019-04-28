from flask import jsonify
from Model.MaterialModel import *


class MaterialController:

    @staticmethod
    def all():
        return jsonify(MaterialModel.all())

    @staticmethod
    def create(data):
        result = MaterialModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
