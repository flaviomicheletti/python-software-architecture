#!/bin/bash

mkdir -p blog/application/services
touch blog/application/services/post_service.py
touch blog/application/services/comment_service.py

mkdir -p blog/application/dtos
touch blog/application/dtos/post_dto.py
touch blog/application/dtos/comment_dto.py

mkdir -p blog/application/repositories
touch blog/application/repositories/post_repository.py
touch blog/application/repositories/comment_repository.py

mkdir -p blog/application/use_cases
touch blog/application/use_cases/create_post.py
touch blog/application/use_cases/update_post.py
touch blog/application/use_cases/delete_post.py
touch blog/application/use_cases/add_comment.py
touch blog/application/use_cases/delete_comment.py

mkdir -p blog/domain/models
touch blog/domain/models/post.py
touch blog/domain/models/comment.py

mkdir -p blog/domain/services
touch blog/domain/services/post_validator.py
touch blog/domain/services/comment_validator.py

mkdir -p blog/infrastructure/persistence
touch blog/infrastructure/persistence/post_repository.py
touch blog/infrastructure/persistence/comment_repository.py
