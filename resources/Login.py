from flask_restful import Resource, reqparse
from models.UserModel import UserModel
from helpers.Helpers import Helpers
from validators.LoginRequest import LoginRequest

helper = Helpers()
message = helper.response_message()['login']


class Login(Resource):

    @classmethod
    def post(cls):
        _parser_login = LoginRequest(reqparse.RequestParser(bundle_errors=True, trim=True))
        _parser_login = _parser_login.validate()

        data = _parser_login.parse_args()
        username = data['username']
        user = UserModel.find_by_username(_username=username)
        user_json = user.json()
        if not user:
            return {
                'message': message['not-found']
            }, 404

        hashed = helper.check_password(data['password'], user_json['password'])
        if hashed:
            return {
                'message': message['succeed'],
                'data': user.json()
            }, 200

        return {
            "message": message['invalid-credential']
        }, 401

