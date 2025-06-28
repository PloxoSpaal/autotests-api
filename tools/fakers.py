from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст.

        :return: Случайный текст.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4.

        :return: Случайный UUID4.
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайный email.

        :return: Случайный email.
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        :return: Случайное предложение.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        :return: Случайный пароль.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя.

        :return: Случайное отчество.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует строку с предполагаемым временем (например, "2 weeks").

        :return: Строка с предполагаемым временем.
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует случайный максимальный балл в диапазоне от 50 до 100.

        :return: Случайный балл.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайный минимальный балл в диапазоне от 1 до 30.

        :return: Случайный балл.
        """
        return self.integer(1, 30)


# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())