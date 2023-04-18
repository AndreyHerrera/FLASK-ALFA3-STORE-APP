class UserRegister():
    def __init__(self, name, lastName, dni, email, password) -> None:
        self.name = name
        self.lastName = lastName
        self.dni = dni
        self.email = email
        self.password = password


def json_to_data_register(user_data):
    name = user_data['name']
    last_name = user_data['lastName']
    dni = user_data['dni']
    email = user_data['email']
    password = user_data['password']
    return UserRegister(name, last_name, dni, email, password)