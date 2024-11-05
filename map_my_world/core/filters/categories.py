from uuid import UUID
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from map_my_world.shared.adapters.db.sql.models.categories import Categories


class CategoriesFilter(Filter):
    status: Optional[bool] = None

    class Constants(Filter.Constants):
        model = Categories