from flask_restful import reqparse
from helpers.RoleValidators import RoleValidator


class UserRegister:

    def __init__(self, _parser):
        self.parser = _parser
        self.customValidator = RoleValidator()

    def validate(self):
        self.parser.add_argument('name',
                                 type=str,
                                 required=True,
                                 help="This Name cannot be blank."
                                 )
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 help="This Username cannot be blank."
                                 )
        self.parser.add_argument('photo_profile',
                                 type=str,
                                 required=True,
                                 help="This Profile Photo cannot be blank."
                                 )
        self.parser.add_argument('phonenumber',
                                 type=str,
                                 required=False
                                 )
        self.parser.add_argument('birthday_place',
                                 type=str,
                                 required=True,
                                 help="This Birthday Place cannot be blank."
                                 )
        self.parser.add_argument('birthday',
                                 type=self.customValidator.date,
                                 required=True,
                                 help="This Birthday cannot be blank."
                                 )
        self.parser.add_argument('address',
                                 type=str,
                                 required=False
                                 )
        self.parser.add_argument('resume',
                                 type=str,
                                 required=False
                                 )
        self.parser.add_argument('headline',
                                 type=str,
                                 required=False
                                 )
        self.parser.add_argument('summary',
                                 type=str,
                                 required=False
                                 )
        self.parser.add_argument('email',
                                 type=self.customValidator.email,
                                 required=True,
                                 help="This Email cannot be blank."
                                 )
        self.parser.add_argument('link_instagram',
                                 type=str,
                                 required=False,
                                 )
        self.parser.add_argument('link_linkedin',
                                 type=str,
                                 required=False,
                                 )
        self.parser.add_argument('link_twitter',
                                 type=str,
                                 required=False,
                                 )
        self.parser.add_argument('link_youtube',
                                 type=str,
                                 required=False,
                                 )
        self.parser.add_argument('link_google_plus',
                                 type=str,
                                 required=False,
                                 )
        self.parser.add_argument('link_facebook',
                                 type=str,
                                 required=False,
                                 )
        self.parser.add_argument('password',
                                 type=str,
                                 required=True,
                                 help="This Password cannot be blank."
                                 )
        self.parser.add_argument('type_theme',
                                 type=str,
                                 required=True,
                                 help="This Type Theme cannot be blank."
                                 )
        return self.parser


class Id:
    def __init__(self, _parser):
        self.parser = _parser

    def validate(self):
        self.parser.add_argument('id',
                                 type=int,
                                 required=True,
                                 help="This Type id cannot be blank."
                                 )
        return self.parser
