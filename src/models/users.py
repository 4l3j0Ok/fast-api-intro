from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


class Success(BaseModel):
    input: str | int | dict = None
    detail: str | User | list[User]


class Failed(BaseModel):
    input: str | int | dict = None
    detail: str = None


class Result(BaseModel):
    success: list[Success] = []
    failed: list[Failed] = []
