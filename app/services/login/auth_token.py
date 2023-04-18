from datetime import datetime, timedelta, time
import secrets

from app.models.user.login import UserLogin
from app.database.database import connection_database
from app.utils.database.query_user import query_create_token_user, query_validated_token_user

def generate_token(user : UserLogin):
    token = str(secrets.token_hex(16))
    created_at = datetime.now()
    expires_at = created_at + timedelta(minutes=30)

    connection = connection_database()
    cursor = connection.cursor()
    cursor.execute(query_create_token_user(user, token, created_at, expires_at))
    connection.commit()
    connection.close()

    return token


def validated_token(token : str):
    connection = connection_database()
    cursor = connection.cursor()
    cursor.execute(query_validated_token_user(token))
    expires_at = cursor.fetchall()[0][0]
    connection.close()
    time_token = ((expires_at - datetime.now()).total_seconds() / 60)
    
    if 0 <= time_token <= 30:
        print("Bien")

    else:
        print("mal")