from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    visit = db.Column(db.Integer(11), default=None)
    remember_token = db.Column(db.String(100), default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=None)
    deleted_at = db.Column(db.TIMESTAMP, default=None, comment="for soft delete")

    def __init__(self, name, username, photo_profile, phonenumber, birthday_place, birthday,
                 address, resume, headline, summary, email, link_instagram, link_linkedin,
                 link_twitter, link_youtube, link_google_plus, link_facebook, email_verified_at,
                 password, type_theme, visit, remember_token, created_at, updated_at, deleted_at):
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
        self.email_verified_at = email_verified_at
        self.password = password
        self.type_theme = type_theme
        self.visit = visit
        self.remember_token = remember_token
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
