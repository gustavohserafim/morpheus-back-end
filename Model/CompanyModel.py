from App.DB import *


class CompanyModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'name', 'cnpj', 'logo', 'phone', 'address'], 'company')

    @staticmethod
    def create(data):
        return DB.insert(data, 'company')

    @staticmethod
    def get(company_id):
        return DB.SelectById(company_id, ['id', 'name', 'cnpj', 'logo', 'phone', 'address'], 'company')

    @staticmethod
    def remove(company_id):
        return DB.remove(company_id, 'company')
