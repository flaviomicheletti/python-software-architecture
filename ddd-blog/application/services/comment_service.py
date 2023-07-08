from blog.domain.models.comment import Comment
from blog.application.repositories.comment_repository import CommentRepository

class CommentService:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def add_comment(self, post_id, content):
        comment = Comment(content)
        self.comment_repository.add_comment(post_id, comment)

    def delete_comment(self, comment_id):
        comment = self.comment_repository.get_comment_by_id(comment_id)
        if comment:
            self.comment_repository.delete_comment(comment)

    def get_comments_for_post(self, post_id):
        return self.comment_repository.get_comments_for_post(post_id)
