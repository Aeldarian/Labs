class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages
    def __str__(self):
        str1 = f'Книга "{self.name}"'
        return str1
    def __repr__(self):
        str1 = f"Book(id_={str(self.id)}, name='{self.name}', pages={str(self.pages)})"
        return str1


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
