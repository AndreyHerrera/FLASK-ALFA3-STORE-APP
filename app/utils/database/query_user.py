from app.models.user.register import UserRegister
from app.models.user.login import UserLogin
from app.utils.user.encrypt import encrypt_password


query_table_user = """
        CREATE TABLE IF NOT EXISTS user_app (id SERIAL PRIMARY KEY, name VARCHAR(256) NOT NULL, last_name VARCHAR(256) NOT NULL,
         dni BIGINT CHECK (dni >= 0 AND dni <= 9999999999) NOT NULL, email VARCHAR(256) NOT NULL, password VARCHAR(256) NOT NULL);
    """

query_table_token = """
        CREATE TABLE IF NOT EXISTS user_token_app (id SERIAL PRIMARY KEY, email VARCHAR(256) NOT NULL, token VARCHAR(32) NOT NULL,
         created_at timestamp  NOT NULL, expires_at timestamp NOT NULL);
    """

def query_register_user(user : UserRegister) -> str:
    query = f"""
        INSERT INTO public.user_app
        (name, last_name, dni, email, password)
        VALUES('{user.name}', '{user.lastName}', {user.dni}, '{user.email}', '{encrypt_password(user.password)}');
    """

    return query


def query_login_user(user : UserLogin):
    query = f"""
        SELECT * FROM public.user_app WHERE email = '{user.email}' and password = '{encrypt_password(user.password)}';
    """

    return query


def query_create_token_user(user: UserLogin, token, created_at, expires_at):
    query = f"""
        INSERT INTO public.user_token_app
        (email, token, created_at, expires_at) VALUES('{user.email}', '{token}', '{created_at}', '{expires_at}')
    """

    return query


def query_validated_token_user(token : str):
    query = f"""
        SELECT expires_at FROM public.user_token_app WHERE token = '{token}';
    """

    return query