from datetime import datetime
from db import db
from sqlalchemy import or_
from helpers.General import General


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(191), nullable=False)
    username = db.Column(db.String(191), nullable=False, comment="must Unique")
    photo_profile = db.Column(db.Text, nullable=False)
    phonenumber = db.Column(db.String(191), default=None, comment="must Unique")
    birthday_place = db.Column(db.String(191), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    address = db.Column(db.Text, default=None)
    resume = db.Column(db.Text, default=None)
    headline = db.Column(db.String(191), default=None)
    summary = db.Column(db.Text, default=None)
    email = db.Column(db.String(191), nullable=False, comment="must Unique")
    link_instagram = db.Column(db.String(191), default=None)
    link_linkedin = db.Column(db.String(191), default=None)
    link_twitter = db.Column(db.String(191), default=None)
    link_youtube = db.Column(db.String(191), default=None)
    link_google_plus = db.Column(db.String(191), default=None)
    link_facebook = db.Column(db.String(191), default=None)
    email_verified_at = db.Column(db.TIMESTAMP, default=None)
    password = db.Column(db.String(191), nullable=False)
    type_theme = db.Column(db.String(100), nullable=False)
    visit = db.Column(db.Integer(), default=0)
    remember_token = db.Column(db.String(100), default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=None)
    deleted_at = db.Column(db.TIMESTAMP, default=None, comment="for soft delete")

    def __init__(self, name, username, photo_profile, phonenumber, birthday_place, birthday,
                 address, resume, headline, summary, email, link_instagram, link_linkedin,
                 link_twitter, link_youtube, link_google_plus, link_facebook,
                 password, type_theme):
        self.name = name
        self.username = username
        self.photo_profile = photo_profile
        self.phonenumber = phonenumber
        self.birthday_place = birthday_place
        self.birthday = birthday
        self.address = address
        self.resume = resume
        self.headline = headline
        self.summary = summary
        self.email = email
        self.link_instagram = link_instagram
        self.link_linkedin = link_linkedin
        self.link_twitter = link_twitter
        self.link_youtube = link_youtube
        self.link_google_plus = link_google_plus
        self.link_facebook = link_facebook
        self.password = General.password_hash(password)
        self.type_theme = type_theme

    def json(self, message):
        return {
            'message': message,
            'data': {
                'id': self.id,
                'name': self.name,
                'username': self.username,
                'photo_profile': self.photo_profile,
                'phonenumber': self.phonenumber,
                'birthday_place': self.birthday_place,
                'birthday': "{}-{}-{}".format(self.birthday.year, self.birthday.month, self.birthday.day),
                'address': self.address,
                'resume': self.resume,
                'headline': self.headline,
                'summary': self.summary,
                'email': self.email,
                'link_instagram': self.link_instagram,
                'link_linkedin': self.link_linkedin,
                'link_twitter': self.link_twitter,
                'link_youtube': self.link_youtube,
                'link_google_plus': self.link_google_plus,
                'link_facebook': self.link_facebook,
                'email_verified_at': "{}".format(self.email_verified_at) if self.email_verified_at else None,
                'password': self.password,
                'type_theme': self.type_theme,
                'visit': self.visit,
                'created_at': "{}".format(self.created_at) if self.created_at else None,
                'updated_at': "{}".format(self.updated_at) if self.updated_at else None,
                'deleted_at': "{}".format(self.deleted_at) if self.deleted_at else None,
            }
        }

    def save(self):
        self.created_at = datetime.now()
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated_at = datetime.now()
        db.session.commit()

    def delete(self):
        self.deleted_at = datetime.now()
        db.session.commit()

    @classmethod
    def find_all(cls, _name, _username, _birthday, _phonenumber, _email, message):
        filters = []
        response = []

        if _name is not None:
            filters.append(cls.name == _name)
        if _username is not None:
            filters.append(cls.username == _username)
        if _birthday is not None:
            filters.append(cls.birthday == _birthday)
        if _phonenumber is not None:
            filters.append(cls.phonenumber == _phonenumber)
        if _email is not None:
            filters.append(cls.email == _email)

        if filters is not None:
            users = cls.query.filter(or_(*filters)).all()
            for user in users:
                response.append(
                    {
                        'id': user.id,
                        'name': user.name,
                        'username': user.username,
                        'photo_profile': user.photo_profile,
                        'phonenumber': user.phonenumber,
                        'birthday_place': user.birthday_place,
                        'birthday': "{}-{}-{}".format(user.birthday.year, user.birthday.month, user.birthday.day),
                        'address': user.address,
                        'resume': user.resume,
                        'headline': user.headline,
                        'summary': user.summary,
                        'email': user.email,
                        'link_instagram': user.link_instagram,
                        'link_linkedin': user.link_linkedin,
                        'link_twitter': user.link_twitter,
                        'link_youtube': user.link_youtube,
                        'link_google_plus': user.link_google_plus,
                        'link_facebook': user.link_facebook,
                        'email_verified_at': "{}".format(user.email_verified_at) if user.email_verified_at else None,
                        'password': user.password,
                        'type_theme': user.type_theme,
                        'visit': user.visit,
                        'created_at': "{}".format(user.created_at) if user.created_at else None,
                        'updated_at': "{}".format(user.updated_at) if user.updated_at else None,
                        'deleted_at': "{}".format(user.deleted_at) if user.deleted_at else None,
                    }
                )
        else:
            users = cls.query.all()
            for user in users:
                response.append(
                    {
                        'id': user.id,
                        'name': user.name,
                        'username': user.username,
                        'photo_profile': user.photo_profile,
                        'phonenumber': user.phonenumber,
                        'birthday_place': user.birthday_place,
                        'birthday': "{}-{}-{}".format(user.birthday.year, user.birthday.month, user.birthday.day),
                        'address': user.address,
                        'resume': user.resume,
                        'headline': user.headline,
                        'summary': user.summary,
                        'email': user.email,
                        'link_instagram': user.link_instagram,
                        'link_linkedin': user.link_linkedin,
                        'link_twitter': user.link_twitter,
                        'link_youtube': user.link_youtube,
                        'link_google_plus': user.link_google_plus,
                        'link_facebook': user.link_facebook,
                        'email_verified_at': "{}".format(user.email_verified_at) if user.email_verified_at else None,
                        'password': user.password,
                        'type_theme': user.type_theme,
                        'visit': user.visit,
                        'created_at': "{}".format(user.created_at) if user.created_at else None,
                        'updated_at': "{}".format(user.updated_at) if user.updated_at else None,
                        'deleted_at': "{}".format(user.deleted_at) if user.deleted_at else None,
                    }
                )

        return {
            'message': message,
            'data': response
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id, deleted_at=None).first()

    @classmethod
    def find_by_username(cls, _username, method_update=False, _id=None):
        if method_update:
            return cls.query.filter(cls.username == _username, cls.deleted_at == None, id != _id).first()
        return cls.query.filter_by(username=_username, deleted_at=None).first()

    @classmethod
    def find_by_email(cls, _email, method_update=False, _id=None):
        if method_update:
            return cls.query.filter(cls.email == _email, cls.deleted_at == None, id != _id).first()
        return cls.query.filter_by(email=_email, deleted_at=None).first()

    @classmethod
    def find_by_phonenumber(cls, _phonenumber, method_update=False, _id=None):
        if method_update:
            return cls.query.filter(cls.phonenumber == _phonenumber, cls.deleted_at == None, id != _id).first()
        return cls.query.filter_by(phonenumber=_phonenumber, deleted_at=None).first()
