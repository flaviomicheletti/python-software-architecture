from blog.application.repositories.comment_repository import CommentRepository

class GetCommentsForPost:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, post_id):
        return self.comment_repository.get_comments_for_post(post_id)
