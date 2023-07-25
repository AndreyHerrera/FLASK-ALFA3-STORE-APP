from datetime import datetime, timedelta
import secrets

from flask import Blueprint, request, jsonify
from app.models.user.auth_token import json_to_data_auth_token

from app.models.user.login import UserLogin
from app.database.database import connection_database
from app.utils.database.query_user import query_add_time_token_user, query_create_token_user, query_validated_token_user

AUTH_TOKEN = Blueprint('AUTH_TOKEN', __name__)

@AUTH_TOKEN.route('/V1/authToken', methods=['POST'])
def validated_token():
    try:
        get_token = json_to_data_auth_token(request.get_json())
        connection = connection_database()
        cursor = connection.cursor()
        cursor.execute(query_validated_token_user(str(get_token.token)))
        expires_at = cursor.fetchall()[0][0]
        time_token = ((expires_at - datetime.now()).total_seconds() / 60)
        
        if 0 <= time_token <= 5:
            new_expires_at = datetime.now() + timedelta(minutes=5)
            cursor.execute(query_add_time_token_user(str(get_token.token), new_expires_at))
            connection.commit()
            connection.close()
            return jsonify({'AuthToken' : True}), 200

        else:
            connection.close()
            return jsonify({'AuthToken' : True}), 401
        
    except Exception as exc:
        return {'Error' : exc}, 200


def generate_token(user : UserLogin):
    try:
        token = str(secrets.token_hex(16))
        created_at = datetime.now()
        expires_at = created_at + timedelta(minutes=5)

        connection = connection_database()
        cursor = connection.cursor()
        cursor.execute(query_create_token_user(user, token, created_at, expires_at))
        connection.commit()
        connection.close()

        return token

    except Exception as exc:
        return {'Error' : exc}, 200