class Comment:
    def __init__(self,user,content, like = 0):
        self.username = user
        self.content = content
        self.likes = like

comment = Comment("user1", "I like this book")

print(comment.username)

print(comment.content)

print(comment.likes)