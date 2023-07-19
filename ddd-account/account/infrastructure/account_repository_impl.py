from application.repositories import AccountRepository
from domain.account import Account

class AccountRepositoryImpl(AccountRepository):
    def __init__(self, database):
        self.database = database

    def get_account(self, account_number):
        # Implementation specific to retrieve an account from the database
        # Assuming the database has a table named "accounts" with columns "account_number" and "balance"
        account_data = self.database.query("SELECT * FROM accounts WHERE account_number = ?", account_number)
        if account_data:
            account_number = account_data["account_number"]
            balance = account_data["balance"]
            return Account(account_number, balance)
        return None

    def save_account(self, account):
        # Implementation specific to save an account to the database
        # Assuming the database has a table named "accounts" with columns "account_number" and "balance"
        self.database.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)",
                              account.account_number, account.balance)

    def delete_account(self, account_number):
        # Implementation specific to delete an account from the database
        # Assuming the database has a table named "accounts" with columns "account_number"
        self.database.execute("DELETE FROM accounts WHERE account_number = ?", account_number)
