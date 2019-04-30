from App.DB import *


class AdressModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'client_id', 'type', 'adress'], 'adress')

    @staticmethod
    def create(data):
        return DB.insert(data, 'adress')

