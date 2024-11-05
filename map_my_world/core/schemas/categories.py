from pydantic import BaseModel
from uuid import UUID


class CategoryCreateSchema(BaseModel):
    name: str
    description: str


class CategoryReadSchema(BaseModel):
    id: UUID
    name: str
    description: str
