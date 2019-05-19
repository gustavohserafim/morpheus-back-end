from App.DB import *


class AddressModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'client_id', 'type', 'adress'], 'adress')

    @staticmethod
    def create(data):
        return DB().insert(data, 'adress')

    @staticmethod
    def get(address_id):
        return DB().SelectById(address_id, ['id', 'client_id', 'type', 'adress'], 'adress')

    @staticmethod
    def remove(address_id):
        return DB().remove(address_id, 'adress')
