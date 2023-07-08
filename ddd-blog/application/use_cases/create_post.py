from blog.application.repositories.post_repository import PostRepository
from blog.application.dtos.post_dto import PostDTO
from blog.domain.models.post import Post
from blog.domain.services.post_validator import PostValidator

class CreatePost:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post_dto: PostDTO):
        if PostValidator.is_valid_title(post_dto.title) and PostValidator.is_valid_content(post_dto.content):
            post = Post(post_dto.title, post_dto.content)
            self.post_repository.save(post)
