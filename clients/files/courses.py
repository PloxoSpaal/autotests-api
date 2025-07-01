import pytest
from pydantic import BaseModel
from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.users import UserFixture
from fixtures.files import FileFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(courses_client: CoursesClient,
                    function_user: UserFixture,
                    function_file: FileFixture
                    ) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)