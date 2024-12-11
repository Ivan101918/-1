import doctest


class Dog:
    def __init__(self, name: str, bite_strenght: (int, float),  speed: (int, float)):
        """
        Создание и подготовка к работе объекта "Собака"

        :param bite_strenght: Сила укуса
        :param name: Кличка собаки
        :param speed: Скорость передвижения

        Примеры:
        >> dog1 = Dog('Шарик', 10, 25)  # инициализация экземпляра класса
        """
        if not isinstance(speed, (int, float)):
            raise TypeError('Только численные значения для "параметра скорость"')
        if speed < 0:
            raise ValueError('"Скорость" может быть только неотрицательным числом')
        self.speed = speed

        if not isinstance(name, str):
            raise TypeError('Кличка должна быть строкой')
        if len(name) == 0:
            raise ValueError('Кличка не может быть пустой строкой')
        self.name = name

        if not isinstance(bite_strenght, (int, float)):
            raise TypeError('Только численные значения для параметра "сила укуса"')
        if bite_strenght < 0:
            raise ValueError('"Сила укуса" может быть только неотрицательным числом')
        self.bite_strenght = bite_strenght

    def run(self, range: int) -> None:
        """
        Функция, которая позволяет собаке бежать

        :param range: растояние для пробега

        :raise ValueError: Если заданное расстояние отрицательно

        Примеры:
        >> dog1 = Dog('Шарик', 10, 25)
        >> dog1.run(100)
        """
        ...

    def bite(self) -> None:
        """
        Функция, позволяющая собаке кусаться

        Примеры:
        >> dog1 = Dog('Шарик', 10, 25)
        >> dog1.bite()
        """
        ...

    def change_name(self, new_name: str) -> None:
        """
        Функция, позволяющая дописать заданное количесвто страниц для книги

        :new_name: Новое название книги

        :raise TypeError: Если введен неправильный тип данных
        :raise ValueError: Если введена пустая строка

        Примеры:
        >> dog1 = Dog('Шарик', 10, 25)
        >> dog1.change_name('Бобик')
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
