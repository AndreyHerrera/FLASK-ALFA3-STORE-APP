class UserLogin():
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password


def json_to_data_login(user_data):
    email = user_data['email']
    password = user_data['password']
    return UserLogin(email, password)