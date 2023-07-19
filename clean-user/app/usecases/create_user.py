from app.interfaces.repositories import UserRepository
from app.entities.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username, email):
        user = User(user_id=None, username=username, email=email)
        created_user = self.user_repository.create_user(user)
        return created_user
