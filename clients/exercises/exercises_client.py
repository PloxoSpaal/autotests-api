from typing import TypedDict
import httpx
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class Exercise(TypedDict):
    """
    Описание структуры задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа метода, получающего список заданий
    """
    exercises: list[Exercise]


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> httpx.Response:
        """
        Метод получает список заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        Метод получает информацию о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request_body: CreateExerciseRequestDict) -> httpx.Response:
        """
        Метод создаёт задание.

        :param request_body: Словарь с title, courseId, maxScore,
         minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request_body)

    def update_exercise_api(self, exercise_id: str, request_body: UpdateExerciseRequestDict) -> httpx.Response:
        """
        Метод обновляет данные задания.

        :param exercise_id: Идентификатор задания
        :param request_body: Словарь с title, maxScore,
         minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request_body)

    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        Метод удаляет задание.

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> Exercise:
        """
        Метод возвращает объект в виде структуры Exercise

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта Exercise
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод возвращает обьъект в виде структуры GetExercisesResponseDict

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде структуры GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request_body: CreateExerciseRequestDict) -> Exercise:
        """
        Метод возвращает объект в виде структуры Exercise

        :param request_body: Словарь с title, courseId, maxScore,
         minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде структуры Exercise
        """
        response = self.create_exercise_api(request_body)
        return response.json()

    def update_exercise(self, exercise_id: str, request_body: UpdateExerciseRequestDict) -> Exercise:
        """
        Метод возвращает объект в виде структуры Exercise

        :param exercise_id: Идентификатор задания
        :param request_body: Словарь с title, maxScore,
         minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде структуры Exercise
        """
        response = self.update_exercise_api(exercise_id, request_body)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))