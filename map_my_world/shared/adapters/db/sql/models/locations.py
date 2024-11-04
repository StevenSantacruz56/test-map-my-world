from uuid import UUID
from datetime import datetime
from typing import List
from sqlmodel import (Field, Relationship)
from sqlalchemy import Column

from map_my_world.shared.utils.custom_fields import FloatDecimal
from map_my_world.shared.adapters.db.sql.models.base_class import (TimestampModel, UUIDModel)
from map_my_world.shared.adapters.db.sql.models.categories import Categories


class LocationCategoryReviewLink(UUIDModel, TimestampModel, table=True):
    """Tabla de enlace entre Location y Category con información de revisión"""

    location_id: int = Field(foreign_key="locations.id")
    category_id: int = Field(foreign_key="categories.id")
    last_reviewed_at: datetime = Field(default_factory=datetime.utcnow)
    reviewed_count: int = Field(default=0)

    # Relaciones
    location: "Locations" = Relationship(back_populates="reviews")
    category: "Categories" = Relationship(back_populates="reviews")

    __tablename__ = "location_category_reviewed"


class Locations(UUIDModel, TimestampModel, table=True):
    name: str = Field(nullable=False)
    latitude: float = Field(sa_column=Column(FloatDecimal(20, 10), nullable=False))
    longitude: float = Field(sa_column=Column(FloatDecimal(20, 10), nullable=False))
    status: bool = Field(default=True)

    # Relaciones
    reviews: List[LocationCategoryReviewLink] = Relationship(back_populates="location")

    __tablename__ = "locations"
