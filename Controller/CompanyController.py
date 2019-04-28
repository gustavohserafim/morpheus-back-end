from flask import jsonify
from Model.CompanyModel import *


class CompanyController:

    @staticmethod
    def all():
        return jsonify({'result': 'ok', 'data': CompanyModel.all()}), 200

    @staticmethod
    def create(data):
        result = CompanyModel.create(data)

        if result is False:
            return jsonify({'result': 'error', 'message': 'failed to insert'}), 400
        return jsonify({'result': 'ok'}), 200

    @staticmethod
    def get(company_id):
        return jsonify({'result': 'ok', 'data': CompanyModel.get(company_id)}), 200

    @staticmethod
    def remove(company_id):
        CompanyModel.remove(company_id)
        return jsonify({'result': 'ok'}), 200
