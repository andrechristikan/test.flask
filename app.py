from flask import Flask
from flask_restful import Api

app = Flask(__name__)
# mysql+mysqlconnector://$USER:$PASS@$HOST/$DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@localhost/andrechristikan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.secret_key = 'jose'
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8080, debug=True)
