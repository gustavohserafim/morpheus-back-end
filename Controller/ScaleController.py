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
    @staticmethod
    def get(company_id):
        return jsonify({'result': 'ok', 'data': ScaleModel.get(scale_id)}), 200

    @staticmethod
    def remove(company_id):
        ScaleModel.remove(scale_id)
        return jsonify({'result': 'ok'}), 200
