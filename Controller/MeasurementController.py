from flask import jsonify
from Model.MeasurementModel import *


class MeasurementController:

    @staticmethod
    def all():
        return jsonify(MeasurementModel.all())

    @staticmethod
    def create(data):
        result = MeasurementModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
    @staticmethod
    def get(company_id):
        return jsonify({'result': 'ok', 'data': MeasurementModel.get(measurement_id)}), 200

    @staticmethod
    def remove(company_id):
        MeasurementModel.remove(measurement_id)
        return jsonify({'result': 'ok'}), 200
