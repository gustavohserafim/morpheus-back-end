from flask import jsonify
from Model.CommercialInvoiceModel import *

class CommercialInvoiceController:


    @staticmethod
    def getHome():
        return jsonify(CommercialInvoiceModel.getHome())
    
    @staticmethod
    def all():
        return jsonify(CommercialInvoiceModel.all())

    @staticmethod
    def create(data):
        result = CommercialInvoiceModel.create(data)

        if result is False:
            return jsonify({'error': True, 'message': 'failed to insert', 'code': 400})
        return jsonify({'result': 'ok', 'code': 200})

    @staticmethod
    def get(id):
        return jsonify({'result': 'ok', 'data': CommercialInvoiceModel.get(id)}), 200

    @staticmethod
    def remove(id):
        CommercialInvoiceModel.remove(id)
        return jsonify({'result': 'ok'}), 200
