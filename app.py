from flask import Flask
from flask_restful import Api
from db import db
from helpers.Helpers import Helpers
from routers import Routers

app = Flask(__name__)
configs = Helpers().config_app
for key in configs:
    app.config[key] = configs[key]
api = Api(app)

router = Routers(api)
router.get()

if __name__ == '__main__':
    db.init_app(app)

    app.run(
        port=configs["APP_PORT"],
        debug=configs["DEBUG"],
        host=configs["APP_SERVER"]
    )
