from sqlmodel import Field, Relationship
from typing import List
from map_my_world.shared.adapters.db.sql.models.base_class import (TimestampModel, UUIDModel)
from map_my_world.shared.adapters.db.sql.models.locations import LocationCategoryReviewLink


class Categories(UUIDModel, TimestampModel, table=True):
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    status: bool = Field(default=True)

    __tablename__ = "categories"
