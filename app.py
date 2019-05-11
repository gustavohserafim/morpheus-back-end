from flask import Flask, request
import mysql.connector
from flask_jwt_extended import (
    JWTManager, jwt_required, jwt_refresh_token_required, get_jwt_identity, unset_jwt_cookies
)
from Controller.AuthController import *
from Controller.CompanyController import *
from Controller.MaterialController import *
from Controller.Adm.UserController import *
from Controller.MeasurementController import *
from Controller.MaterialController import *
from Controller.ClientController import *
from Controller.AdressController import *
from Controller.CommercialInvoiceController import *

app = Flask(__name__)

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False  # Set to true in production
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_SECRET_KEY'] = 'adASKninau219378wad212'  # Set with environment variable in production

jwt = JWTManager(app)
mysql = mysql.connector.connect(
 host="162.241.2.234",
 user="ghclim06_morpheu",
  passwd="rSai0ZK1ZG",
  database="ghclim06_morpheus"
)

@app.route('/user', methods=['POST'])
# @jwt_required
def adm_user_create(): 

  return UserController.create(request.get_json())

# Routes
@app.route('/token/auth', methods=['POST'])
def login(): 
  return AuthController.login(request.get_json())


@app.route('/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh(): 
  return AuthController.refresh_token(get_jwt_identity())


@app.route('/token/remove', methods=['DELETE'])
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200


@app.route('/api/company', methods=['GET'])
# @jwt_required
def company_all(): 
  return CompanyController.all()


@app.route('/api/company', methods=['POST'])
# @jwt_required
def company_create(): 
  return CompanyController.create(request.get_json())


@app.route('/client', methods=['GET'])
def client_all(): 
  return ClientController.all()


@app.route('/client', methods=['POST'])
def client_create(): 
  return ClientController.create(request.get_json())


@app.route('/adress', methods=['GET'])
def adress_all(): 
  return AdressController.all()


@app.route('/adress', methods=['POST'])
def adress_create(): 
  return AdressController.create(request.get_json())


@app.route('/material', methods=['GET'])
# @jwt_required
def material_all():
  return MaterialController.all()


@app.route('/material', methods=['POST'])
# @jwt_required
def material_create(): 
  return MaterialController.create(request.get_json())


@app.route('/measurement', methods=['GET'])
# @jwt_required
def measurement_all(): 
  return MeasurementController.all()


@app.route('/measurement', methods=['POST'])
# @jwt_required
def measurement_create(): 
  return MeasurementController.create(request.get_json())


@app.route('/api/company/<int:company_id>', methods=['GET'])
# @jwt_required
def company_get(company_id): 
  return CompanyController.get(company_id)


@app.route('/api/company/<int:company_id>', methods=['DELETE'])
# @jwt_required
def company_remove(company_id): 
  return CompanyController.remove(company_id)


@app.route('/api/home', methods=['GET'])
# @jwt_required
def home(): 
  return CommercialInvoiceController.getHome()
