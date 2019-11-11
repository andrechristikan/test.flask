import datetime
from validate_email import validate_email


class RoleValidator:

    @staticmethod
    def date(value, name):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD.".format(name))

        return value

    @staticmethod
    def email(value, name):
        is_valid = value if validate_email(value) else ValueError("Incorrect email format.".format(name))

        return is_valid

