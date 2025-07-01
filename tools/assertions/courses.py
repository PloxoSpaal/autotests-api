from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base import assert_equal


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")