from App.DB import *


class TransportModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'nome', 'city', 'type'], 'transport')

    @staticmethod
    def create(data):
        return DB.insert(data, 'transport')

