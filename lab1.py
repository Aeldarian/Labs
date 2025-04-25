# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Vehicle:
    def __init__(self, speed: float, fuel: float):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param speed: Максимальная скорость
        :param fuel: Количество топлива

        Примеры:
        >>> car = Vehicle(120, 50)
        """
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        if not isinstance(fuel, (int, float)) or fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным")

        self.speed = speed
        self.fuel = fuel
    def time_to_move_distance(self, distance: float) -> float:
        """
        Перемещение транспортного средства

        :param distance: Расстояние, которое нужно проехать

        :return: Время необходимое для того, чтобы проехать введенное расстояние

        Примеры:
        >>> car = Vehicle(50, 30)
        >>> car.time_to_move_distance(100)
        """
        if not isinstance(distance, (int,float)):
            raise TypeError("Проезжаемое  должна быть типа int или float")
        if distance < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...
    def refuel(self, amount: float) -> None:
        """
        Заправка транспортного средства

        :param amount: Количество добавляемого топлива

        Примеры:
        >>> car = Vehicle(50, 30)
        >>> car.refuel(100)
        """
        if not isinstance(amount, (int,float)):
            raise TypeError("Количество топливо должно быть типа int или float")
        if amount < 0:
            raise ValueError("Добавляемое топливо должно быть положительным числом")
        ...
class Building:
    def __init__(self, height: float, floors: int, doors: int):
        """
        Создание объекта "Здание"
        :param height: Высота здания
        :param floors: Количество этажей

        Примеры:
        >>> house = Building(30, 10,1)
        """
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть положительным целым числом")
        if not isinstance(doors, int) or doors <= 0:
            raise ValueError("Количество дверей должно быть положительным целым числом")

        self.height = height
        self.floors = floors
    def open_door(self) -> None:
        """
        Открытие двери здания

        Примеры:
        >>> house = Building(30, 10,1)
        >>> house.open_door()
        """
        ...
    def rebuild_house(self, height:float, floors: int) -> None:
        """
        Изменение высоты и количества этажей в доме
        :param height: Насколько изменилась высота дома
        :param floors: Насколько изменилось количество этажей в доме

        :raise ValueError: Если количество этажей и изменяемая высота имеют разную полярность, то вызываем ошибку
        :raise ValueError: Если количество этажей и изменяемая высота уходят в минус после изменения , то вызываем ошибку

        Примеры:
        >>> house = Building(30, 10,1)
        >>> house.rebuild_house(-9,-3)
        """
        if not isinstance(height, (int,float)):
            raise TypeError("Высота должна быть типа int или float")
        if not isinstance(floors, (int)):
            raise TypeError("Количество этажей должно быть типа int")
        ...
class Animal:
    def __init__(self, species: str, weight: float):
        """
        Создание объекта "Животное"

        :param species: Вид животного
        :param weight: Вес животного

        Примеры:
        >>> dog = Animal("Собака", 20.5)
        """
        if not isinstance(species, str) or not species:
            raise ValueError("Вид животного должен быть непустой строкой")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес должен быть положительным числом")

        self.species = species
        self.weight = weight
    def make_sound(self) -> None:
        """
        Издание звука животным

        Примеры:
        >>> dog = Animal("Собака", 20.5)
        >>> dog.make_sound()
        """
        ...
    def rename(self, species: str) -> None:
        """
        Изменение вида животного

        :param species: Вид животного
        Примеры:
        >>> dog = Animal("Собака", 20.5)
        >>> dog.rename("Кошка")
        """
        if not isinstance(species, str) or not species:
            raise ValueError("Вид животного должен быть непустой строкой")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

