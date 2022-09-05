class ArticleList:
    def __init__(self, title, slug) -> None:
        super().__init__()
        self.title = title
        self.slug = slug

    title = ""
    slug = ""


class Article:
    def __init__(self, title, body) -> None:
        super().__init__()
        self.title = title
        self.body = body
    title = ""
    body = ""