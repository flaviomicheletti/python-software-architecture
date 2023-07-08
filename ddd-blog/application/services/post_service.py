from blog.domain.models.post import Post
from blog.application.repositories.post_repository import PostRepository

class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def create_post(self, title, content):
        post = Post(title, content)
        self.post_repository.save(post)

    def update_post(self, post_id, title, content):
        post = self.post_repository.get_by_id(post_id)
        if post:
            post.title = title
            post.content = content
            self.post_repository.save(post)

    def delete_post(self, post_id):
        post = self.post_repository.get_by_id(post_id)
        if post:
            self.post_repository.delete(post)
