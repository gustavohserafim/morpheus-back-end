from App.DB import *


class CommercialInvoiceModel:

    @staticmethod
    def getHome():
        return DB().selectFA("SELECT commercial_invoice.id, created_at, name as client_name  FROM commercial_invoice, client WHERE client_id = client.id AND commercial_invoice.removed = 0;")
    
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
        ci = DB().selectFA("SELECT commercial_invoice.id, created_at, name as client_name  FROM commercial_invoice, client WHERE commercial_invoice.id = {} AND client_id = client.id AND commercial_invoice.removed = 0;".format(ci_id))
        ci[0]['created_at'] = ci[0]['created_at'].strftime("%Y-%m-%d")
        return ci

    @staticmethod
    def getMaterials(ci_id):

        items = DB().selectFC("SELECT material_id FROM ci_item WHERE commercial_invoice_id = {} AND removed = 0;".format(ci_id))
        sql = "SELECT id, amount, ncm, name, unit, weight_unit, net_weight, value FROM material WHERE id IN(%s);" % ','.join(['%s'] * len(items))

        return DB().exec(sql, items)

    @staticmethod
    def remove(ci_id):
        return DB().remove(ci_id, 'id')
