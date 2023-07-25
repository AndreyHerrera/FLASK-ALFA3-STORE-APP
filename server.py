from flask import Flask
from flask_cors import CORS

from app.database.database import connection_database
from app.controllers.register.register import REGISTER
from app.controllers.login.login import LOGIN
from app.services.login.auth_token import AUTH_TOKEN

APP = Flask(__name__)
CORS(APP)
APP.register_blueprint(REGISTER)
APP.register_blueprint(LOGIN)
APP.register_blueprint(AUTH_TOKEN)


if __name__ == '__main__':
    connection_database(any)
    APP.run(port = 3000, debug = True)