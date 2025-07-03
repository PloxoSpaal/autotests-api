from http import HTTPStatus
import pytest
import allure
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, assert_create_course_response
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
@allure.suite(AllureSuite.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureSubSuite.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Обновление данных курса")
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(function_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureSubSuite.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Получение списка курсов")
    def test_get_courses(
            self, courses_client: CoursesClient,
            function_user: UserFixture, function_course: CourseFixture):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureSubSuite.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Создание курса")
    def test_create_course(
            self, courses_client: CoursesClient,
            function_user: UserFixture, function_file: FileFixture):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id)
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())