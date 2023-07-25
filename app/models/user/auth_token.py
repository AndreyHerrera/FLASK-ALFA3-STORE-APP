class UserAuthToken():
    def __init__(self, token) -> None:
        self.token = token

def json_to_data_auth_token(user_data):
    token = user_data['AuthToken']
    return UserAuthToken(token)