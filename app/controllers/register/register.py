from flask import Blueprint, request

from app.models.user.register import json_to_data_register
from app.utils.database.query_user import query_register_user
from app.database.database import connection_database

REGISTER = Blueprint('REGISTER', __name__)

@REGISTER.route('/V1/register', methods=['POST'])
def register_user():
    try:
        user_data = json_to_data_register(request.get_json())
        connection = connection_database()
        cursor = connection.cursor()
        cursor.execute(query_register_user(user_data))
        connection.commit()
        connection.close()
        return {'Response' : 'OK'}, 200
    except:
        pass