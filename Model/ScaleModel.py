from App.DB import *


class ScaleModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'balanca'], 'scale')

    @staticmethod
    def create(data):
        return DB.insert(data, 'scale')

