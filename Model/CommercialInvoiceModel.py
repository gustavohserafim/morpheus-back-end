from App.DB import *


class CommercialInvoiceModel:

    @staticmethod
    def getHome():
        return DB().selectAll(['id', 'client_id', 'transport_id'], 'commercial_invoice')
    
    @staticmethod
    def all():
        return DB().selectAll(['id', 'client_id', 'transport_id'], 'commercial_invoice')

    @staticmethod
    def create(data):
        return DB().insert(data, 'commercial_invoice')

    @staticmethod
    def get(CommercialInvoice_id):
        return DB().SelectById(CommercialInvoice_id, ['id', 'client_id', 'transport_id'], 'commercial_invoice')

    @staticmethod
    def remove(CommercialInvoice_id):
        return DB().remove(CommercialInvoice_id, 'id')