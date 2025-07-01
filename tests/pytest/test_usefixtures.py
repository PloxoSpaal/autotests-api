import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")