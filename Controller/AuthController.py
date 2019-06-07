from flask import jsonify
from Model.AuthModel import *
from flask_jwt_extended import set_access_cookies, set_refresh_cookies, unset_jwt_cookies


class AuthController:

    @staticmethod
    def login(request):

        if 'email' not in request or 'password' not in request or len(request['email']) < 1 or len(request['password']) < 1:
            return jsonify({'result': 'error', 'message': 'Missing fields.'}), 400

        token = AuthModel.login(request['email'], request['password'])
        if token is False:
            return jsonify({'result': 'error', 'message': 'Email or password incorrect.'}), 401

        resp = jsonify({'result': 'ok', 'message': 'Login ok', 'data': {'token': token}})

        return resp, 200

    @staticmethod
    def login_dev(request):

        if 'email' not in request or 'password' not in request:
            return jsonify({'result': 'error', 'message': 'Missing fields.'}), 400

        token = AuthModel.login_dev(request['email'], request['password'])
        if token is False:
            return jsonify({'result': 'error', 'message': 'Email or password incorrect.'}), 401

        resp = jsonify({'result': 'ok', 'message': 'Login ok', 'data': {'token': token}})

        return resp, 200



    @staticmethod
    def logout():
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        return resp, 200
