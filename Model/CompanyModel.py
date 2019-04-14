from App.DB import *


class CompanyModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'name', 'cnpj', 'logo', 'phone', 'address'], 'company')

    def