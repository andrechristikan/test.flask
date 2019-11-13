from helpers.CustomValidators import CustomValidator
from helpers.General import General


class UserAddValidator:

    def __init__(self, _parser):
        self.parser = _parser
        self.customValidator = CustomValidator()
        self.message = General().response_message()['validator']

    def validate(self):
        self.parser.add_argument('name',
                                 type=str,
                                 required=True,
                                 help=self.message['required']
                                 )
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 help=self.message['required']
                                 )
        self.parser.add_argument('photo_profile',
                                 type=str,
                                 required=True,
                                 help=self.message['required']
                                 )
        self.parser.add_argument('phonenumber',
                                 type=str,
                                 required=False
                                 )
        self.parser.add_argument('birthday_place',
                                 type=str,
                                 required=True,
                                 help=self.message['required']
                                 )
        self.parser.add_argument('birthday',
                                 type=self.customValidator.date,
                                 required=True,
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
                                 help=self.message['required']
                                 )
        self.parser.add_argument('type_theme',
                                 type=str,
                                 required=True,
                                 help=self.message['required']
                                 )
        return self.parser
