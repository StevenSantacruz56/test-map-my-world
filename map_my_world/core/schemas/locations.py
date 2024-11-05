from pydantic import BaseModel
from uuid import UUID


class LocationCreateSchema(BaseModel):
    name: str
    latitude: float
    longitude: float
    category_id: UUID


class LocationReadSchema(BaseModel):
    id: UUID
    name: str
    latitude: float
    longitude: float
