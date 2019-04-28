from App.DB import *


class ScaleModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'balanca'], 'scale')

    @staticmethod
    def create(data):
        return DB.insert(data, 'scale')

    @staticmethod
    def get(scale_id):
        return DB.SelectById(scale_id, ['id'], 'scale')

    @staticmethod
    def remove(scale_id):
        return DB.remove(scale_id, 'scale')