from app.models.user.register import User
from app.utils.user.encrypt import encrypt_password


query_table_user = """
        CREATE TABLE IF NOT EXISTS user_app (id SERIAL PRIMARY KEY, name VARCHAR(256) NOT NULL, last_name VARCHAR(256) NOT NULL,
         dni BIGINT CHECK (dni >= 0 AND dni <= 9999999999) NOT NULL, email VARCHAR(256) NOT NULL, password VARCHAR(256) NOT NULL);
    """

def query_register_user(user : User) -> str:
    query = f"""
        INSERT INTO public.user_app
        ("name", last_name, dni, email, "password")
        VALUES('{user.name}', '{user.lastName}', {user.dni}, '{user.email}', '{encrypt_password(user.password)}');
    """

    return query