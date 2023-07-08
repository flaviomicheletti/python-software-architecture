from blog.domain.models.post import Post
from blog.application.repositories.post_repository import PostRepository

class PostRepository:
    def __init__(self):
        self.posts = []

    def save(self, post: Post):
        if post not in self.posts:
            self.posts.append(post)

    def delete(self, post: Post):
        if post in self.posts:
            self.posts.remove(post)

    def get_by_id(self, post_id):
        for post in self.posts:
            if post.id == post_id:
                return post

    def get_all(self):
        return self.posts
