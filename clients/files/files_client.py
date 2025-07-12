from httpx import Response
import allure
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.routes import APIRoutes
from clients.api_coverage import tracker


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Get file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    @tracker.track_coverage_httpx(APIRoutes.FILES)
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": request.upload_file.read_bytes()}
        )

    @allure.step("Create file body")
    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

    @allure.step("Delete file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.FILES}/{file_id}")


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))