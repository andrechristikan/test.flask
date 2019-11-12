from flask import Flask
from flask_restful import Api
from resources.User import UserFindById, UserFindByUsername, User

app = Flask(__name__)
# mysql+pymysql://$USER:$PASS@$HOST/$DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/andrechristikan-clone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.secret_key = 'jose'
api = Api(app)

api.add_resource(UserFindByUsername, '/r/<string:username>')
api.add_resource(UserFindById, '/user/<int:user_id>')
api.add_resource(User, '/user')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8080, debug=True)
