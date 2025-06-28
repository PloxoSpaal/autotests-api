from tools.assertions.base import assert_equal
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema


def assert_created_user_values(
        actual: CreateUserResponseSchema, expected: CreateUserRequestSchema):
    """
    Проверка соответствия значений ответа значениям запроса
    метода создания пользователя api/v1/users/create

    :param expected: Тело запроса api/v1/users/create со значениями
    :param actual: Тело ответа со api/v1/users/create значениями
    :return: AssertionError при несоответствии значений
    """
    assert_equal(actual.user.email, expected.email, 'email')
    assert_equal(actual.user.first_name, expected.first_name, 'first_name')
    assert_equal(actual.user.middle_name, expected.middle_name, 'middle_name')
    assert_equal(actual.user.last_name, expected.last_name, 'last_name')