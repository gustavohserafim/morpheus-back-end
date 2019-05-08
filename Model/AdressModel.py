from App.DB import *


class AdressModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'client_id', 'type', 'adress'], 'adress')

    @staticmethod
    def create(data):
        return DB.insert(data, 'adress')

    @staticmethod
    def get(adress_id):
        return DB.SelectById(adress_id, ['id', 'client_id', 'type', 'adress'], 'adress')

    @staticmethod
    def remove(adress_id):
        return DB.remove(adress_id, 'adress')
