from section_3.blog.post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"<Blog({self.title}, {self.author}, {self.posts})"

    def create_post(self, **kwargs):
        self.posts.append(Post(title=kwargs.get('title'), content=kwargs.get('content')))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }
