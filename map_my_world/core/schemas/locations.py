from pydantic import BaseModel
from uuid import UUID

class LocationCreateSchema(BaseModel):
    name: str
    latitude: float
    longitude: float

class LocationReadSchema(BaseModel):
    id: UUID
    name: str
    latitude: float
    longitude: float