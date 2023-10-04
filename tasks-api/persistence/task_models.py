from sqlmodel import SQLModel, Field
from ulid import ulid


class UserBase(SQLModel):
    login: str = Field(nullable=False, unique=True)
    name: str = Field(min_length=6)


class UserCreate(UserBase):
    password: str = Field(min_length=6)


class User(UserBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)
    password: str

    @staticmethod
    def from_user_create(user_create: UserCreate):
        user = User()
        user.login = user_create.login
        user.name = user_create.name
        user.password = user_create.password
        return user 