from flask import Flask, request
from flask_mysqldb import MySQL
from Controller.CompanyController import *
from Controller.MeasurementController import *
from Controller.MaterialController import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'M3SrwmVxfO'
app.config['MYSQL_PASSWORD'] = 'rSai0ZK1ZG'
app.config['MYSQL_DB'] = 'M3SrwmVxfO'

mysql = MySQL(app)

# Routes
@app.route('/company', methods=['GET'])
def company_all(): return CompanyController.all()


@app.route('/company', methods=['POST'])
def company_create(): return CompanyController.create(request.get_json())

@app.route('/material', methods=['GET'])
def material_all(): return MaterialController.all()

@app.route('/material', methods=['POST'])
def material_create(): return MaterialController.create(request.get_json())

@app.route('/measurement', methods=['GET'])
def measurement_all(): return MeasurementController.all()

@app.route('/measurement', methods=['POST'])
def measurement_create(): return MeasurementController.create(request.get_json())