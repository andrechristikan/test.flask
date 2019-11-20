from helpers.Helpers import Helpers
from validators.Rules import Rules


class LoginRequest:
    def __init__(self, _parser):
        self.parser = _parser
        self.rule = Rules()
        self.message = Helpers().response_message()['validator']

    def validate(self):
        self.parser.add_argument('username',
                                 type=self.rule.non_empty_string,
                                 required=True,
                                 location='form',
                                 trim=True,
                                 nullable=False,
                                 help=self.message['required']
                                 )
        self.parser.add_argument('password',
                                 type=self.rule.non_empty_string,
                                 required=True,
                                 location='form',
                                 trim=True,
                                 nullable=False,
                                 help=self.message['required']
                                 )
        return self.parser
