from flask import jsonify
from Model.CommercialInvoiceModel import *


class CommercialInvoiceController:

    @staticmethod
    def getHome():
        homes = CommercialInvoiceModel.getHome()

        for k, v in enumerate(homes):
            homes[k]['created_at'] = homes[k]['created_at'].strftime("%Y-%m-%d")
        return jsonify({'data': homes}), 200
    
    @staticmethod
    def all():
        return jsonify(CommercialInvoiceModel.all())

    @staticmethod
    def create(data):
        result = CommercialInvoiceModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert'}), 400
        return jsonify({'result': 'ok', 'created_id': result['id']}), 200

    @staticmethod
    def get(id):
        return jsonify({'result': 'ok', 'data': CommercialInvoiceModel.get(id)}), 200

    @staticmethod
    def remove(id):
        CommercialInvoiceModel.remove(id)
        return jsonify({'result': 'ok'}), 200
