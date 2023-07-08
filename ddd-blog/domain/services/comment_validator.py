class CommentValidator:
    @staticmethod
    def is_valid_content(content):
        return isinstance(content, str) and len(content) > 0
