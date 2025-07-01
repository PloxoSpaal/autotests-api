from typing import Any, Sized


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(expected)}. '
        f'Actual length: {len(actual)}'
    )


def assert_status_code(actual: int, expected: int):
    """
    Проверка соответствия фактического статус-кода ожидаемому

    :param actual: Фактический статус-код
    :param expected: Ожидаемый статус-код
    :return: AssertionError если статус-коды не совпадают
    """
    assert actual == expected, (
        f'Incorrect status code: expect {expected}, got {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверка соответствия фактического значения ожидаемому

    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Название ключа
    :return: AssertionError если значения не совпадают
    """
    assert actual == expected, (
        f'''Incorrect value in "{name}":
            expect "{expected}", got "{actual}"'''
    )


def assert_value_is_true(value: Any, key: str):
    """
    Проверка наличия значения у ключа

    :param value: Проверяемое значение
    :param key: Ключ проверяемого значения
    :return: AssertionError при пустом значении
    """
    assert value, (
        f'Incorrect value "{value}" in "{key}"'
    )