class CommentRepository:
    def __init__(self):
        self.comments = {}

    def add_comment(self, post_id, comment):
        if post_id not in self.comments:
            self.comments[post_id] = []
        self.comments[post_id].append(comment)

    def delete_comment(self, comment):
        for post_id, post_comments in self.comments.items():
            if comment in post_comments:
                post_comments.remove(comment)
                break

    def get_comment_by_id(self, comment_id):
        for post_comments in self.comments.values():
            for comment in post_comments:
                if comment.id == comment_id:
                    return comment

    def get_comments_for_post(self, post_id):
        return self.comments.get(post_id, [])
