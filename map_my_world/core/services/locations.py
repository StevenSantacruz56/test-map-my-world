from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from map_my_world.core.services.generic import GenericService
from map_my_world.shared.adapters.db.sql.models.locations import Locations, LocationCategoryReviewLink
from map_my_world.shared.adapters.db.sql.models import Categories
from map_my_world.shared.adapters.db.sql.decorators import atomic
from map_my_world.core.schemas.locations import LocationReadSchema, LocationCreateSchema

from map_my_world.shared.adapters.db.sql.models import Locations


class LocationsService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.generic_service = GenericService(session)

    async def get_location_by_id(self, location_id: UUID) -> Locations:
        result = await self.generic_service.get_by_primary_key(key=location_id, model=Locations)
        return result

    async def list(self, limit: int = 10, offset: int = 0, location_filter: object = None) -> list[Locations]:
        statement = select(Locations)
        if location_filter:
            statement = location_filter.filter(statement)
        statement = statement.offset(offset)
        statement = statement.limit(limit)
        results = await self.session.exec(statement)
        return results.all()

    @atomic
    async def create(self, location_create: LocationCreateSchema) -> LocationReadSchema:
        location = await self.__create_location__(location_create)
        review = await self.__create_location_category_review_link__(location.id, location_create.category_id)
        result = await self.__get_location_category_review_link__(review.id)
        return location

    async def __create_location__(self, location_create) -> Locations:
        location = Locations(**location_create.dict())
        self.session.add(location)
        await self.session.flush()
        return location

    async def __create_location_category_review_link__(self, location_id, category_id) -> LocationCategoryReviewLink:
        location_category_review_link = LocationCategoryReviewLink(location_id=location_id, category_id=category_id)
        self.session.add(location_category_review_link)
        await self.session.flush()
        return location_category_review_link

    async def __get_location_category_review_link__(self, location_review_id) -> LocationCategoryReviewLink:
        statement = (
            select(LocationCategoryReviewLink)
            .join(Locations, Locations.id ==
                  LocationCategoryReviewLink.location_id)
            .join(Categories, Categories.id ==
                  LocationCategoryReviewLink.category_id)
            .where(LocationCategoryReviewLink.id == location_review_id)
        )
        results = await self.session.exec(statement)
        return results.all()
