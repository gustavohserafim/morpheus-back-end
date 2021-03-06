from flask import Flask, request
from os import environ
from flask_jwt_extended import (
    JWTManager, jwt_required
)
from Controller.AuthController import *
from Controller.CompanyController import *
from Controller.Adm.UserController import *
from Controller.MeasurementController import *
from Controller.MaterialController import *
from Controller.ClientController import *
from Controller.AddressController import *
from Controller.CommercialInvoiceController import *
from Controller.TransportController import *
from Controller.Ci_itemController import *

app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = environ['SECRET_KEY']
app.config['JWT_HEADER_TYPE'] = ''

# Routes
@app.route('/user', methods=['POST'])
@jwt_required
def adm_user_create():
    return UserController.create(request.get_json())


@app.route('/api/auth', methods=['POST'])
def login():
    return AuthController.login(request.get_json())


@app.route('/api/auth/dev', methods=['POST'])
def login_dev():
    return AuthController.login_dev(request.get_json())


@app.route('/api/auth', methods=['DELETE'])
@jwt_required
def logout():
    return AuthController.logout()


@app.route('/api/company', methods=['GET'])
@jwt_required
def company_all():
    return CompanyController.all()


@app.route('/api/company', methods=['POST'])
@jwt_required
def company_create():
    return CompanyController.create(request.get_json())


@app.route('/api/client', methods=['GET'])
@jwt_required
def client_all():
    return ClientController.all()


@app.route('/api/client', methods=['POST'])
@jwt_required
def client_create():
    return ClientController.create(request.get_json())


@app.route('/api/client/<int:client_id>', methods=['GET', 'PUT', 'DELETE'])
# @jwt_required
def client_ud(client_id):
    data = request.get_json()
    if request.method == 'PUT':
        return ClientController.update(client_id, data)
    elif request.method == 'DELETE':
        return ClientController.remove(client_id)
    else:
        return ClientController.get(client_id)


@app.route('/api/ci', methods=['GET'])
@jwt_required
def ci_all():
    return CommercialInvoiceController.all()


@app.route('/api/ci', methods=['POST'])
@jwt_required
def create_ci():
    return CommercialInvoiceController.create(request.get_json())


@app.route('/api/ci/<int:ci_id>', methods=['GET'])
@jwt_required
def ci_get(ci_id):
    return CommercialInvoiceController.get(ci_id)


@app.route('/api/address', methods=['GET'])
@jwt_required
def address_all():
    return AddressController.all()


@app.route('/api/address', methods=['POST'])
@jwt_required
def address_create():
    return AddressController.create(request.get_json())


@app.route('/api/material', methods=['GET'])
@jwt_required
def material_all():
    return MaterialController.all()


@app.route('/api/material', methods=['POST'])
@jwt_required
def material_create():
    return MaterialController.create(request.get_json())


@app.route('/api/material/<int:material_id>', methods=['PUT'])
@jwt_required
def material_update(material_id):
    return MaterialController.update(material_id, request.get_json())


@app.route('/api/measurement', methods=['GET'])
@jwt_required
def measurement_all():
    return MeasurementController.all()


@app.route('/api/measurement', methods=['POST'])
@jwt_required
def measurement_create():
    return MeasurementController.create(request.get_json())


@app.route('/api/measurement/<int:measurement_id>', methods=['PUT'])
@jwt_required
def measurement_update(measurement_id):
    data = request.get_json()
    return MeasurementController.update(measurement_id, data)


@app.route('/api/company/<int:company_id>', methods=['GET'])
@jwt_required
def company_get(company_id):
    return CompanyController.get(company_id)


@app.route('/api/company/<int:company_id>', methods=['DELETE'])
@jwt_required
def company_remove(company_id):
    return CompanyController.remove(company_id)


@app.route('/api/home', methods=['GET'])
@jwt_required
def home():
    return CommercialInvoiceController.getHome()


@app.route('/api/transport', methods=['GET'])
@jwt_required
def get_transport():
    return TransportController.all()


@app.route('/api/ci_item', methods=['POST'])
@jwt_required
def ci_item_create():
    return Ci_itemController.create(request.get_json())
