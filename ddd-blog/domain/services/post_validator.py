class PostValidator:
    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title) > 0

    @staticmethod
    def is_valid_content(content):
        return isinstance(content, str) and len(content) > 0
