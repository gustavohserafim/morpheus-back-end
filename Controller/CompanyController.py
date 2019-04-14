from flask import jsonify
from Model.CompanyModel import *


class CompanyController:

    @staticmethod
    def all():
        return jsonify(CompanyModel.all())

    @staticmethod
    def create(data):
        result = CompanyModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
