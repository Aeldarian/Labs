class Animal:
    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор класса Animal.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Инкапсуляция: имя не должно изменяться напрямую
        self.age = age
    def __str__(self) -> str:
        return f'Животное"{self.name}"'
    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"
    def make_sound(self) -> str:
        """
        Метод, который должен быть переопределён в дочерних классах для издания звуков.
        """
        raise NotImplementedError("Этот метод должен быть переопределён в дочернем классе.")
class Dog(Animal):
    """Класс, представляющий собаку, наследуется от Animal."""
    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def __repr__(self) -> str:
        """
        Перегруженный метод для отображения информации о собаке.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"
    def make_sound(self) -> str:
        """
        Переопределённый метод. Собака лает.
        """
        return "Гав-гав!"
class Cat(Animal):
    """
    Класс, представляющий кошку, наследуется от Animal.
    """
    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Конструктор класса Cat.

        :param name: Имя кошки
        :param age: Возраст кошки
        :param color: Окрас кошки
        """
        super().__init__(name, age)
        self.color = color

    def __repr__(self) -> str:
        """
        Перегруженный метод для отображения информации о кошке.
        """
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"
    def make_sound(self) -> str:
        """
        Переопределённый метод. Кошка мяукает.
        """
        return "Мяу-мяу!"
if __name__ == "__main__":
    dog = Dog("Бобик", 3, "Овчарка")
    cat = Cat("Мурка", 2, "Рыжий")
    print(dog)
    print(dog.make_sound())
    print(cat)
    print(cat.make_sound())
