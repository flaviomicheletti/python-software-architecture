from blog.application.repositories.comment_repository import CommentRepository
from blog.application.dtos.comment_dto import CommentDTO
from blog.domain.models.comment import Comment

class AddComment:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, post_id, comment_dto: CommentDTO):
        comment = Comment(comment_dto.content)
        self.comment_repository.add_comment(post_id, comment)
