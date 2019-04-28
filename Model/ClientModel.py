from App.DB import *


class ClientModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'name', 'phone', 'fax', 'contact'], 'client')

    @staticmethod
    def create(data):
        return DB.insert(data, 'client')

