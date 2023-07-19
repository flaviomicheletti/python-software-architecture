from app.interfaces.input_ports import CreateUserInputPort
from app.usecases.create_user import CreateUserUseCase


class CreateUserInputAdapter(CreateUserInputPort):
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    def create_user(self, username, email):
        return self.create_user_use_case.execute(username, email)
