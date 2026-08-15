from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.exceptions.auth import EmailAlreadyRegisteredError, InvalidCredentialsError

class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def signup(self, name: str, email: str, password: str):
        existing = self.repository.get_by_email(email)
        if existing:
            raise EmailAlreadyRegisteredError()
        user = self.repository.create(name=name, email=email, password_hash=hash_password(password))
        token = create_access_token({"sub": str(user.id)})
        return user, token

    def login(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()
        token = create_access_token({"sub": str(user.id)})
        return user, token