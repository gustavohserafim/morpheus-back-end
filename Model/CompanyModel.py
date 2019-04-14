from App.DB import *


class CompanyModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'name', 'cnpj', 'logo', 'phone', 'address'], 'company')

    @staticmethod
    def create(data):
        return DB.insert(data, 'company')

