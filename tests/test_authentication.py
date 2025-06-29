from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import get_authentication_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_user_client = get_public_users_client()
    auth_client = get_authentication_client()
    request = CreateUserRequestSchema()
    public_user_client.create_user_api(request)
    login_response = auth_client.login_api(request)
    login_response_body = LoginResponseSchema.model_validate_json(login_response.text)
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_body)
    validate_json_schema(login_response.json(), login_response_body.model_json_schema())