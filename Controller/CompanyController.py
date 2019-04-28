from flask import jsonify
from Model.CompanyModel import *


class CompanyController:

    @staticmethod
    def all():
        return jsonify({'result': 'ok', 'code': 200, 'data': CompanyModel.all()})

    @staticmethod
    def create(data):
        result = CompanyModel.create(data)

        if result is False:
            return jsonify({'result': 'error', 'code': 400, 'message': 'failed to insert'})
        return jsonify({'result': 'ok', 'code': 200})

    @staticmethod
    def get(company_id):
        return jsonify({'result': 'ok', 'code': 200, 'data': CompanyModel.get(company_id)})

    @staticmethod
    def remove(company_id):
        CompanyModel.remove(company_id)
        return jsonify({'result': 'ok', 'code': 200})
