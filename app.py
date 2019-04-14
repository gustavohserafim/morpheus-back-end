from flask import Flask
from flask_mysqldb import MySQL
from Controller.CompanyController import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'M3SrwmVxfO'
app.config['MYSQL_PASSWORD'] = 'rSai0ZK1ZG'
app.config['MYSQL_DB'] = 'M3SrwmVxfO'

mysql = MySQL(app)


@app.route('/company', methods=['GET'])
def company_all():
    return CompanyController.all()
