from typing import List
from sqlmodel import (Field, Relationship)

from map_my_world.shared.adapters.db.sql.models.base_class import (TimestampModel, UUIDModel)


class Categories(UUIDModel, TimestampModel, table=True):
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    status: bool = Field(default=True)

    reviews_category: List["LocationCategoryReviewLink"] = Relationship(back_populates="category") # noqa F821

    __tablename__ = "categories"
