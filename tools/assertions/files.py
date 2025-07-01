from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.url, expected.url, 'url')
    assert_equal(actual.filename, expected.filename, 'filename')
    assert_equal(actual.directory, expected.directory, 'directory')


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


def assert_get_file_response(
        get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(get_file_response.file, create_file_response.file)


def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустая директория.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)
