from domain.account import Account


class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, account_number, initial_balance):
        account = Account(account_number, initial_balance)
        self.account_repository.save_account(account)

    def deposit(self, account_number, amount):
        account = self.account_repository.get_account(account_number)
        account.deposit(amount)
        self.account_repository.save_account(account)

    def withdraw(self, account_number, amount):
        account = self.account_repository.get_account(account_number)
        account.withdraw(amount)
        self.account_repository.save_account(account)

    def get_balance(self, account_number):
        account = self.account_repository.get_account(account_number)
        return account.get_balance()
