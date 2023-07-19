from abc import ABC, abstractmethod


class CreateUserInputPort(ABC):
    @abstractmethod
    def create_user(self, username, email):
        pass
