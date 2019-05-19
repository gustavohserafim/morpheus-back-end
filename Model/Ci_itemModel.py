from App.DB import *


class Ci_itemModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'commercial_invoice_id', 'measurement_unit_id','material_id'], 'ci_item')

    @staticmethod
    def create(data):
        return DB().insert(data, 'ci_item')

    @staticmethod
    def get(ci_item_id):
        return DB().SelectById(ci_item_id, ['id', 'commercial_invoice_id', 'measurement_unit_id','material_id'], 'ci_item')

    @staticmethod
    def remove(ci_item_id):
        return DB().remove(ci_item_id, 'ci_item')



# select from ci_item 
# where commercial_invoice_id = id(commercial_invoice)