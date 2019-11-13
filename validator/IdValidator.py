from helpers.General import General


class IdValidator:
    def __init__(self, _parser):
        self.parser = _parser
        self.message = General().response_message()['validator']

    def validate(self):
        self.parser.add_argument('id',
                                 type=int,
                                 required=True,
                                 help=self.message['required']
                                 )
        return self.parser
