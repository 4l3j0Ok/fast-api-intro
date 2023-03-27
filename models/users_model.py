from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
