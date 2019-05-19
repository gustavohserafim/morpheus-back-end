from App.DB import *


class ClientModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'name', 'phone', 'fax', 'contact'], 'client')

    @staticmethod
    def create(data):
        return DB().insert(data, 'client')

    @staticmethod
    def get(client_id):
        return DB().SelectById(client_id, ['id', 'name', 'phone', 'fax', 'contact'], 'client')

    @staticmethod
    def remove(client_id):
        return DB().remove(client_id, 'client')