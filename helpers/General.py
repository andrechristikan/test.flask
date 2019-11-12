import bcrypt


class General:

    @staticmethod
    def password_hash(password):
        salt = bcrypt.gensalt(rounds=16)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)
        return hashed

    @staticmethod
    def check_password(password, password_hashed):
        checked = bcrypt.checkpw(password.encode('utf8'), password_hashed)
        return checked
