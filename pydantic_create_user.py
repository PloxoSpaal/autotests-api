from pydantic import BaseModel, Field, EmailStr


# Неполная модель данных пользователя
class ShortUserSchema(BaseModel):
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


# Полная модель данных пользователя
class UserSchema(ShortUserSchema):
    id: str


# Запрос на создание пользователя
class CreateUserRequestSchema(ShortUserSchema):
    password: str


# Ответ с данными созданного пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema