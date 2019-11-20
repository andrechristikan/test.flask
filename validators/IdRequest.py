from helpers.Helpers import Helpers


class IdRequest:
    def __init__(self, _parser):
        self.parser = _parser
        self.message = Helpers().response_message()['validator']

    def validate(self):
        self.parser.add_argument('id',
                                 type=int,
                                 required=True,
                                 location='form',
                                 help=self.message['required']
                                 )
        return self.parser
