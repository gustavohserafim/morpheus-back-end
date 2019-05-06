from flask import jsonify
from Model.CommercialInvoiceModel import *

class CommercialInvoiceController:


    @staticmethod
    def getHome():
        return jsonify(CommercialInvoiceModel.getHome())
