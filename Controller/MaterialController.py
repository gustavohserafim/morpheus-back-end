from flask import jsonify
from Model.MaterialModel import *


class MaterialController:

    @staticmethod
    def all():
        return jsonify({'data': MaterialModel.all()})

    @staticmethod
    def create(data):
        result = MaterialModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})

    @staticmethod
    def update(material_id, data):
        result = MaterialModel.update(material_id, data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to update', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})
    
    @staticmethod
    def get(material_id):
        return jsonify({'result': 'ok', 'data': MaterialModel.get(material_id)}), 200

    @staticmethod
    def remove(company_id):
        MaterialModel.remove(company_id)
        return jsonify({'result': 'ok'}), 200
