from http import HTTPStatus
import pytest
import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema
from clients.exercises.exercises_client import ExercisesClient


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:

    @allure.title("Создание задания")
    def test_create_exercise(
            self, exercises_client: ExercisesClient,
            function_course: CourseFixture):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.title("Получение данных задания")
    def test_get_exercise(
            self, exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(
            get_exercise_response=response_data,
            create_exercise_response=function_exercise.response)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.title("Обновление данных задания")
    def test_update_exercise(
            self, exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.title("Удаление задания")
    def test_delete_exercise(
            self, exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture):
        exercise_id = function_exercise.response.exercise.id
        response = exercises_client.delete_exercise_api(exercise_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        get_response = exercises_client.get_exercise_api(exercise_id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())


    @allure.title("Получение списка заданий")
    def test_get_exercises(
            self, exercises_client: ExercisesClient,
            function_course: CourseFixture, function_exercise: ExerciseFixture):
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), response_data.model_json_schema())