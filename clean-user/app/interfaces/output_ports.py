from abc import ABC, abstractmethod


class CreateUserOutputPort(ABC):
    @abstractmethod
    def user_created(self, user):
        pass
