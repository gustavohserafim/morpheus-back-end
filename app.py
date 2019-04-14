from flask import Flask, request
from flask_mysqldb import MySQL
from Controller.CompanyController import *

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


@app.route('/company/<int:company_id>', methods=['GET'])
def company_get(company_id): return CompanyController.get(company_id)

