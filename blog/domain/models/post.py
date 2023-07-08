class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.published = False

    def publish(self):
        self.published = True

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nPublished: {self.published}"
