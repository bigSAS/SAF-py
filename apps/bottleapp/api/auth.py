from api.model import User

def authenticate(email: str, password: str) -> User:
    raise NotImplementedError('todo! return User')


def get_jwt(user: User) -> str:
    raise NotImplementedError('todo! return jwt')
