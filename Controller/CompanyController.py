from flask import jsonify
from Model.CompanyModel import *


class CompanyController:

    @staticmethod
    def all():
        return jsonify(CompanyModel.all())

    @staticmethod
    def create(data):
        return jsonify(CompanyModel.create(data))
