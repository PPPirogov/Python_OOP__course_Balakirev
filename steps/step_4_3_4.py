class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

book = Book('dsad', 'author', 321, 1991)
print(book.__dict__)