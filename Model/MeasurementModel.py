from App.DB import *


class MeasurementModel:

    @staticmethod
    def all():
        return DB().selectAll(['id', 'name', 'description'], 'measurement_unit')

    @staticmethod
    def create(data):
        return DB().insert(data, 'measurement_unit')

    @staticmethod
    def get(measurement_id):
        return DB().SelectById(measurement_id, ['id', 'name', 'description'], 'measurement_unit')

    @staticmethod
    def remove(measurement_id):
        return DB().remove(measurement_id, 'measurement_unit')