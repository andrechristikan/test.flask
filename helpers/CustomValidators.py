import datetime
from validate_email import validate_email
from helpers.General import General


class CustomValidator:

    @staticmethod
    def date(value, name):
        message = General().response_message()['validator']
        if value is None or value == "":
            raise ValueError(message['required'])

        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError(message['date-invalid'])

        return value

    @staticmethod
    def email(value, name):
        message = General().response_message()['validator']
        if value is None or value == "":
            raise ValueError(message['required'])

        is_valid = value if validate_email(value) else ValueError(message['email-invalid'])

        return is_valid

