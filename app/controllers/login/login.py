from flask import Blueprint, request, jsonify

from app.models.user.login import json_to_data_login
from app.database.database import connection_database
from app.services.login.auth_token import generate_token, validated_token
from app.utils.database.query_user import query_login_user


LOGIN = Blueprint('LOGIN', __name__)

@LOGIN.route('/V1/login', methods=['POST'])
def login_user():
    try:
        user_data = json_to_data_login(request.get_json())
        connection = connection_database()
        cursor = connection.cursor()
        cursor.execute(query_login_user(user_data))
        data = cursor.fetchall()
        connection.close()

        if data:
            token = generate_token(user_data)
            return jsonify({'AuthToken' : token}), 200

        else:
            return jsonify({'AuthToken' : False}), 200
    
    except Exception as exc:
        return {'Response' : exc}, 500
        