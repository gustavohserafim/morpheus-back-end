from App.DB import *


class MaterialModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'ncm', 'name'], 'material')

    @staticmethod
    def create(data):
        created_ids = []
        for i in data:
            if DB().insert(i, 'material') is False:
                return False
            created_ids.append(DB().selectFV("SELECT MAX(id) as id FROM material;")['id'])

        return created_ids

    @staticmethod
    def update(material_id, data):
        return DB().update(material_id, data, 'material')

    @staticmethod
    def get(material_id):
        return DB().SelectById(material_id, ['id', 'ncm', 'name', 'description'], 'material')

    @staticmethod
    def remove(material_id):
        return DB().remove(material_id, 'material')