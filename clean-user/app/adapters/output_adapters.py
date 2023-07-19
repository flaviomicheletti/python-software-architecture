from app.interfaces.output_ports import CreateUserOutputPort


class CreateUserOutputAdapter(CreateUserOutputPort):
    def user_created(self, user):
        print(f"User created: {user.username} ({user.email})")
