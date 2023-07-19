class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email
