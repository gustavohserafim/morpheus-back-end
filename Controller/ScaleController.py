from flask import jsonify
from Model.ScaleModel import *


class ScaleController:

    @staticmethod
    def all():
        return jsonify(ScaleModel.all())

    @staticmethod
    def create(data):
        result = ScaleModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
