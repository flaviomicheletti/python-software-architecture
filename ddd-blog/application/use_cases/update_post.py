from blog.application.repositories.post_repository import PostRepository
from blog.application.dtos.post_dto import PostDTO
from blog.domain.services.post_validator import PostValidator

class UpdatePost:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post_id, post_dto: PostDTO):
        post = self.post_repository.get_by_id(post_id)
        if post:
            if PostValidator.is_valid_title(post_dto.title) and PostValidator.is_valid_content(post_dto.content):
                post.title = post_dto.title
                post.content = post_dto.content
                self.post_repository.save(post)
