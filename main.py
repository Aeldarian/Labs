class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, (int)) or pages <= 0:
            raise ValueError("Страницы должны быть положительным числом")
        self.pages = pages
    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Страницы должны быть положительным целым числом")
        self._pages = value
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = duration
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
              raise ValueError("Длительность должна быть положительным числом")
        self._duration = value
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

if __name__ == '__main__':
    book=PaperBook("dada","adda",256);
    print(book)  # проверяем метод __str__

