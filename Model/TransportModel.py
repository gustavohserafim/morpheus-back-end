from App.DB import *


class TransportModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'name', 'city', 'type'], 'transport')

    @staticmethod
    def create(data):
        return DB.insert(data, 'transport')

    @staticmethod
    def get(transport_id):
        return DB.SelectById(transport_id, ['id', 'nome', 'city', 'type'], 'transport')

    @staticmethod
    def remove(transport_id):
        return DB.remove(transport_id, 'transport')