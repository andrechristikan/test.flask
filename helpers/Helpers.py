import bcrypt
import json


class Helpers:

    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)

        self.config_db = self.config['db']

        self.config_app = self.config['app']
        self.config_app['SQLALCHEMY_DATABASE_URI'] = str(
            self.config_app['SQLALCHEMY_DATABASE_URI']
        ).format(
            self.config_db['DATABASE_ENGINE'],
            self.config_db['DATABASE_USERNAME'],
            self.config_db['DATABASE_PASSWORD'],
            self.config_db['DATABASE_SERVER'],
            self.config_db['DATABASE_PORT'],
            self.config_db['DATABASE_NAME'],
            self.config_db['DATABASE_CHARSET']
        )

        self.config_other = self.config['other']
        self.config_jwt = self.config['jwt']

    def password_hash(self, password):
        salt = bcrypt.gensalt(rounds=int(self.config_other['SALT_ROUND']))
        hashed = bcrypt.hashpw(password.encode(self.config_other['PASSWORD_ENCODE']), salt)
        return hashed

    def check_password(self, password, password_hash):
        # hashed = self.password_hash(password)
        if bcrypt.checkpw(
                password.encode(
                    self.config_other['PASSWORD_ENCODE']
                ),
                password_hash.encode(
                    self.config_other['PASSWORD_ENCODE']
                )
        ):
            return True
        return False

    def response_message(self):
        with open('Languages/'+self.config_other['LANGUAGE_PACK']+'.json') as f:
            message = json.load(f)
        return message

    def config_app(self):
        return json.loads(self.config_app)

    def config_jwt(self):
        return json.loads(self.config_jwt)

    def config_other(self):
        return json.loads(self.config_other)
