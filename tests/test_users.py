from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_created_user_values
import pytest


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_body = CreateUserResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_created_user_values(response_body, request)
    validate_json_schema(response.json(), response_body.model_json_schema())


