import psycopg2

from env import os
from app.utils.database.query_user import query_table_user, query_table_token

def connection_database(key = None):
    try:
        connection = psycopg2.connect(
            host = os.getenv('DATASOURCE_HOST'),
            port = os.getenv('DATASOURCE_PORT'),
            user = os.getenv('DATASOURCE_USERNAME'),
            password = os.getenv('DATASOURCE_PASSWORD'),
            dbname = os.getenv('DATASOURCE_SCHEMA')
            )
        
        if key == None:
            return connection
        
        else:
            cursor = connection.cursor()
            cursor.execute(query_table_user)
            cursor.execute(query_table_token)
            connection.commit()
            cursor.close()
            connection.close()

    except Exception as ex:
        print("Database connection failed due to {}".format(ex))