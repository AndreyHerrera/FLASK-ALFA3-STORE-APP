from flask import Flask

from app.database.database import connection_database
from app.controllers.register.register import REGISTER

APP = Flask(__name__)
APP.register_blueprint(REGISTER)


if __name__ == '__main__':
    connection_database(any)
    APP.run(port = 3000, debug = True)