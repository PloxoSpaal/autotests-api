from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.users_schema import CreateUserRequestSchema
from fixtures.users import UserFixture
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.allure.tags import AllureTag
import pytest
import allure


@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:

    @allure.title("Авторизация пользователя")
    def test_login(self,
            authentication_client: AuthenticationClient,
            function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_body = LoginResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_body)
        validate_json_schema(response.json(), response_body.model_json_schema())