from http import HTTPStatus
from config import settings
import pytest
import allure
from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_create_file_with_empty_filename_response, \
    assert_create_file_with_empty_directory_response, assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response, assert_get_file_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.parent_suite import AllureParentSuite
from tools.allure.features import AllureFeature
from tools.allure.suite import AllureSuite
from tools.allure.stories import AllureStory
from tools.allure.sub_suite import AllureSubSuite
from allure_commons.types import Severity


@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.FILES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@pytest.mark.files
@pytest.mark.regression
class TestFiles:

    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureSubSuite.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Создание файла")
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @pytest.mark.xdist_group(name="files-group")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureSubSuite.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Получение файла")
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureSubSuite.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Создание файла с пустым названием")
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/image.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.severity(Severity.MINOR)
    @allure.sub_suite(AllureSubSuite.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Создание файла с пустой директорией")
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file="./testdata/files/image.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @pytest.mark.xdist_group(name="files-group")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureSubSuite.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Удаление файла")
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)
        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())


    @allure.severity(Severity.MINOR)
    @allure.sub_suite(AllureSubSuite.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Получение файла по некорректному file_id")
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        response = files_client.get_file_api(file_id="incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())