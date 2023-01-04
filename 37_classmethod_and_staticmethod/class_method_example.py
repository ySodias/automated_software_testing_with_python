class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        """
        Factory

        :param name:
        :param page_weight:
        :return:
        """
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        """
        Factory

        :param name:
        :param page_weight:
        :return:
        """
        return Book(name, Book.TYPES[1], page_weight + 100)


book = Book.hardcover("Cronicas de Narnia", 300)
print(book)