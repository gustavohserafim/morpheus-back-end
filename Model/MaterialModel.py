from App.DB import *


class MaterialModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'ncm', 'name', 'description'], 'material')

    @staticmethod
    def create(data):
        print(data)
        return DB.insert(data, 'material')

    @staticmethod
    def get(material_id):
        return DB.SelectById(material_id, ['id', 'ncm', 'name', 'description'], 'material')

    @staticmethod
    def remove(material_id):
        return DB.remove(material_id, 'material')