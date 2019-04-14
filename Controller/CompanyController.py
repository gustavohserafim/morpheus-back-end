from flask import jsonify
from Model.CompanyModel import *


class CompanyController:

    @staticmethod
    def all():
        return jsonify(CompanyModel.all())
