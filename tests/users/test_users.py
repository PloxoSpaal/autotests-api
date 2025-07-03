from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_created_user_values, assert_get_user_response
import pytest
import allure
from tools.fakers import fake
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@pytest.mark.users
@pytest.mark.regression
class TestUsers:

    @allure.title("Создание пользователя")
    @allure.story(AllureStory.CREATE_ENTITY)
    @pytest.mark.parametrize(
        "email", [fake.email(domain) for domain in ['mail.ru', 'gmail.com', 'example.com']])
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=email)
        response = public_users_client.create_user_api(request)
        response_body = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_created_user_values(response_body, request)
        validate_json_schema(response.json(), response_body.model_json_schema())


    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Получение информации о пользователе")
    def test_get_user_me(self, private_users_client, function_user):
        response = private_users_client.get_user_me_api()
        response_body = GetUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(
            get_user_response=response_body, create_user_response=function_user.response)
        validate_json_schema(response.json(), response_body.model_json_schema())