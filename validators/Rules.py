import datetime
from validate_email import validate_email
from helpers.Helpers import Helpers

helper = Helpers()


class Rules:

    @staticmethod
    def date(value, name):
        message = helper.response_message()['validator']
        if value is None or value == "":
            raise ValueError(message['required'])

        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError(message['date-invalid'])

        return value

    @staticmethod
    def email(value, name):
        message = helper.response_message()['validator']
        if value is None or value == "":
            raise ValueError(message['required'])

        if validate_email(value):
            value = value
        else:
            raise ValueError(message['email-invalid'])

        return value

    @staticmethod
    def non_empty_string(value, name):
        message = helper.response_message()['validator']
        if value is None or value == "":
            raise ValueError(message['required'])
        return value
