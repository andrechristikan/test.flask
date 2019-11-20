from validators.Rules import Rules
from helpers.Helpers import Helpers


class UserRequest:

    def __init__(self, _parser):
        self.parser = _parser
        self.rule = Rules()
        self.message = Helpers().response_message()['validator']

    def validate(self):
        self.parser.add_argument('name',
                                 type=str,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        self.parser.add_argument('photo_profile',
                                 type=str,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        self.parser.add_argument('phonenumber',
                                 type=str,
                                 required=False,
                                 location='form'
                                 )
        self.parser.add_argument('birthday_place',
                                 type=str,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        self.parser.add_argument('birthday',
                                 type=self.rule.date,
                                 required=True,
                                 location='form',
                                 )
        self.parser.add_argument('address',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('resume',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('headline',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('summary',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('email',
                                 type=self.rule.email,
                                 required=True,
                                 location='form',
                                 )
        self.parser.add_argument('link_instagram',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('link_linkedin',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('link_twitter',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('link_youtube',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('link_google_plus',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('link_facebook',
                                 type=str,
                                 required=False,
                                 location='form',
                                 )
        self.parser.add_argument('password',
                                 type=str,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        self.parser.add_argument('type_theme',
                                 type=str,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        return self.parser
