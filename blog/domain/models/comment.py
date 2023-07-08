class Comment:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"Content: {self.content}"
