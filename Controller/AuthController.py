from flask import jsonify
from Model.AuthModel import *
from flask_jwt_extended import set_access_cookies, set_refresh_cookies


class AuthController:

    @staticmethod
    def login(request):
        login = AuthModel.login(request['email'], request['password'])
        if login is False:
            return jsonify({'result': 'error', 'message': 'Email or password incorrect.'}), 401

        resp = jsonify({'result': 'ok', 'message': 'Login ok'})
        set_access_cookies(resp, login['access_token'])
        set_refresh_cookies(resp, login['refresh_token'])
        return resp, 200

    @staticmethod
    def refresh_token(jwt_identity):
        access_token = create_access_token(identity=jwt_identity)
        resp = jsonify({'result': 'ok', 'message': 'Refresh ok'})
        set_access_cookies(resp, access_token)
        return resp, 200

    # @staticmethod
    # def logout():
