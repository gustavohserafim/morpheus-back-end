from App.DB import *


class MaterialModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'ncm', 'name', 'description'], 'material')

    @staticmethod
    def create(data):
        return DB.insert(data, 'material')

