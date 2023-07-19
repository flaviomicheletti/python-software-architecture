from abc import ABC, abstractmethod

class AccountRepository(ABC):
    @abstractmethod
    def get_account(self, account_number):
        pass

    @abstractmethod
    def save_account(self, account):
        pass

    @abstractmethod
    def delete_account(self, account_number):
        pass
