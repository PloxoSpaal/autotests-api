from tools.assertions.base import assert_equal
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создагние задания соответствует данным из запроса.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с созданным заданием.
    :return AssertionError: Если данные не совпадают.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")