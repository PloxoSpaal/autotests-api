from tools.assertions.base import assert_equal, assert_value_is_true
from clients.authentication.authentication_schema import LoginResponseSchema
import allure
from tools.logger import get_logger


logger = get_logger("AUTHENTICATION_ASSERTIONS")


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверка ответа логина /api/v1/authentication/login

    :param response: Ответ метода /api/v1/authentication/login
    :return: AssertionError при ошибке сравнения
    """
    logger.info("Check login response")
    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_value_is_true(response.token.access_token, 'access_token')
    assert_value_is_true(response.token.refresh_token, 'refresh_token')
