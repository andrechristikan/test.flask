from flask_restful import Resource, reqparse
from models.UserModel import UserModel
from roles.UserRole import UserRegister as RoleUserRegister, Id as RoleId


class UserRegister(Resource):
    def __init__(self):
        self._parser_register = RoleUserRegister(reqparse.RequestParser())
        self._parser_register = self._parser_register.validate()

    def post(self):
        data = self._parser_register.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        elif UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400
        elif UserModel.find_by_phonenumber(data['phonenumber']):
            return {"message": "A user with that phone number already exists"}, 400

        user = UserModel(
            data['name'],
            data['username'],
            data['photo_profile'],
            data['phonenumber'],
            data['birthday_place'],
            data['birthday'],
            data['address'],
            data['resume'],
            data['headline'],
            data['summary'],
            data['email'],
            data['link_instagram'],
            data['link_linkedin'],
            data['link_twitter'],
            data['link_youtube'],
            data['link_google_plus'],
            data['link_facebook'],
            data['password'],
            data['type_theme']
        )
        user.save()

        return {"message": "User created successfully."}, 201


class UserFindByUsername(Resource):
    @classmethod
    def get(cls, username: str):
        user = UserModel.find_by_username(username)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200


class UserFindById(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200


class User(Resource):
    @classmethod
    def delete(cls):
        _parser = RoleId(reqparse.RequestParser())
        _parser = _parser.validate()
        data = _parser.parse_args()

        user = UserModel.find_by_id(data['id'])
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete()
        return {'message': 'User deleted.'}, 200

    @classmethod
    def put(cls):
        _parser_id = RoleId(reqparse.RequestParser())
        _parser_id = _parser_id.validate()

        _parser_register = RoleUserRegister(reqparse.RequestParser())
        _parser_register = _parser_register.validate()

        _id = _parser_id.parse_args()['id']
        data = _parser_register.parse_args()

        user = UserModel.find_by_id(_id)
        # user.


        # if not user:
        #     return {'message': 'User Not Found'}, 404
        # user.delete()
        # return {'message': 'User deleted.'}, 200