from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа метода, получающего список заданий
    """
    exercises: list[ExerciseSchema]