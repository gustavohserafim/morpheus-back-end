from App.DB import *


class Ci_itemModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'commercial_invoice_id', 'measurement_unit_id', 'material_id'], 'ci_item')

    @staticmethod
    def create(data):
        created_ids = []
        for i in data:
            if DB().insert(i, 'ci_item') is False:
                return False
            created_ids.append(DB().selectFV("SELECT MAX(id) as id FROM ci_item;"))

        return created_ids

    @staticmethod
    def get(ci_item_id):
        return DB().SelectById(ci_item_id, ['id', 'commercial_invoice_id', 'measurement_unit_id','material_id'], 'ci_item')

    @staticmethod
    def remove(ci_item_id):
        return DB().remove(ci_item_id, 'ci_item')
