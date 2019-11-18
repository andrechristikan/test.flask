from flask_restful import Resource, reqparse
from models.UserModel import UserModel
from validator.UserValidators import UserAddValidator
from validator.IdValidator import IdValidator
from helpers.General import General

helper = General()
message = helper.response_message()['user']


class UserFindByUsername(Resource):
    @classmethod
    def get(cls, username: str):
        user = UserModel.find_by_username(username)
        if not user:
            return {
                'message': message['not-found']
            }, 404

        return {
            'message': message['single-found'],
            'data': user.json()
         }, 200


class UserFindById(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {
                'message': message['not-found']
            }, 404

        return {
            'message': message['single-found'],
            'data': user.json()
         }, 200


class User(Resource):
    @classmethod
    def get(cls, name=None, username=None, birthday=None, phonenumber=None, email=None):
        users = UserModel.find_all(name, username, birthday, phonenumber, email)

        return {
            'message': message['single-found'],
            'data': users
         }, 200

    @classmethod
    def post(cls):
        _parser_register = UserAddValidator(reqparse.RequestParser(bundle_errors=True))
        _parser_register = _parser_register.validate()

        data = _parser_register.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                "message": message['username-exist']
            }, 400
        elif UserModel.find_by_email(data['email']):
            return {
                "message": message['email-exist']
            }, 400
        elif UserModel.find_by_phonenumber(data['phonenumber']):
            return {
                "message": message['phonenumber-exist']
            }, 400

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

        return {
            'message': message['inserted'],
            'data': user.json()
        }, 201

    @classmethod
    def delete(cls):
        _parser = IdValidator(reqparse.RequestParser(bundle_errors=True))
        _parser = _parser.validate()
        data = _parser.parse_args()

        user = UserModel.find_by_id(data['id'])
        if not user:
            return {
                'message': message['not-found']
            }, 404
        user.delete()

        return {
            'message': message['deleted']
        }, 200

    @classmethod
    def put(cls):
        _parser_id = IdValidator(reqparse.RequestParser(bundle_errors=True))
        _parser_id = _parser_id.validate()

        _parser_register = UserAddValidator(reqparse.RequestParser())
        _parser_register = _parser_register.validate()

        _id = _parser_id.parse_args()['id']
        data = _parser_register.parse_args()

        user = UserModel.find_by_id(_id)
        if not user:
            return {
                'message': message['not-found']
            }, 404
        elif UserModel.find_by_username(data['username'], True, _id):
            return {
                "message": message['username-exist']
            }, 400
        elif UserModel.find_by_email(data['email'], True, _id):
            return {
                "message": message['email-exist']
            }, 400
        elif UserModel.find_by_phonenumber(data['phonenumber'], True, _id):
            return {
                "message": message['phonenumber-exist']
            }, 400

        user.name = data['name']
        user.username = data['username']
        user.photo_profile = data['photo_profile']
        user.phonenumber = data['phonenumber']
        user.birthday_place = data['birthday_place']
        user.birthday = data['birthday']
        user.address = data['address']
        user.resume = data['resume']
        user.headline = data['headline']
        user.summary = data['summary']
        user.email = data['email']
        user.link_instagram = data['link_instagram']
        user.link_linkedin = data['link_linkedin']
        user.link_twitter = data['link_twitter']
        user.link_youtube = data['link_youtube']
        user.link_google_plus = data['link_google_plus']
        user.link_facebook = data['link_facebook']
        user.type_theme = data['type_theme']

        if data['password'] or data['password'] != "":
            user.password = helper.password_hash(data['password'])

        user.update()

        return {
            'message': message['updated'],
            'data': user.json()
        }, 200
