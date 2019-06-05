from flask import Flask, request
from os import environ
from flask_jwt_extended import (
    JWTManager, jwt_required, jwt_refresh_token_required, get_jwt_identity
)
from Controller.AuthController import *
from Controller.CompanyController import *
from Controller.Adm.UserController import *
from Controller.MeasurementController import *
from Controller.MaterialController import *
from Controller.ClientController import *
from Controller.AddressController import *
from Controller.CommercialInvoiceController import *
from Controller.CiController import *

app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = environ['SECRET_KEY']
app.config['JWT_HEADER_TYPE'] = ''


@app.route('/user', methods=['POST'])
@jwt_required
def adm_user_create():
    return UserController.create(request.get_json())

# Routes
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
    return CiController.all()


@app.route('/api/ci', methods=['POST'])
@jwt_required
def ci_create():
    return CiController.create(request.get_json())


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


@app.route('/api/measurement', methods=['GET'])
@jwt_required
def measurement_all():
    return MeasurementController.all()


@app.route('/api/measurement', methods=['POST'])
@jwt_required
def measurement_create():
    return MeasurementController.create(request.get_json())


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
