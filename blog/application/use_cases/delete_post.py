from blog.application.repositories.post_repository import PostRepository

class DeletePost:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post_id):
        post = self.post_repository.get_by_id(post_id)
        if post:
            self.post_repository.delete(post)
