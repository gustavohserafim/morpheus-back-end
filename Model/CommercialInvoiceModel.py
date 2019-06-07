from App.DB import *


class CommercialInvoiceModel:

    @staticmethod
    def getHome():
        return DB().selectFA("SELECT commercial_invoice.id, created_at, name as client_name  FROM commercial_invoice, client WHERE client_id = client.id;")
    
    @staticmethod
    def all():
        return DB().selectAll(['id', 'client_id', 'transport_id'], 'commercial_invoice')

    @staticmethod
    def create(data):
        if DB().insert(data, 'commercial_invoice') is False:
            return False
        return DB().selectFV("SELECT MAX(id) as id FROM commercial_invoice;")

    @staticmethod
    def get(ci_id):
        return DB().SelectById(ci_id, ['id', 'client_id', 'transport_id'], 'commercial_invoice')

    @staticmethod
    def remove(ci_id):
        return DB().remove(ci_id, 'id')