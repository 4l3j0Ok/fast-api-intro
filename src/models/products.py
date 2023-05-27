from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float


class Success(BaseModel):
    input: str | int | dict = None
    detail: str | Product | list[Product]


class Failed(BaseModel):
    input: str | int | dict = None
    detail: str = None


class Result(BaseModel):
    success: list[Success] = []
    failed: list[Failed] = []
