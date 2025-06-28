from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence())
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score())
    min_score: int = Field(alias='minScore', default_factory=fake.min_score())
    description: str = Field(default_factory=fake.text())
    preview_file_id: str = Field(alias='previewFileId', default_factory=fake.uuid4())
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time())
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=fake.uuid4())


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence())
    maxScore: int | None = Field(alias='maxScore', default_factory=fake.max_score())
    minScore: int | None = Field(alias='minScore', default_factory=fake.min_score())
    description: str | None = Field(default_factory=fake.text())
    estimatedTime: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time())