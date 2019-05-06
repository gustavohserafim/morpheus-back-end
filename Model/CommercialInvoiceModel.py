from App.DB import *

class CommercialInvoiceModel:


    @staticmethod
    def getHome():
        return DB.selectAll(['id', 'client_id'], 'commercial_invoice')
