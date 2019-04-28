from App.DB import *


class MeasurementModel:

    @staticmethod
    def all():
        return DB.selectAll(['id', 'name', 'description'], 'measurement_unit')

    @staticmethod
    def create(data):
        return DB.insert(data, 'measurement_unit')
