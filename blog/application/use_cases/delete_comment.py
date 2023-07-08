from blog.application.repositories.comment_repository import CommentRepository

class DeleteComment:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id):
        comment = self.comment_repository.get_comment_by_id(comment_id)
        if comment:
            self.comment_repository.delete_comment(comment)
