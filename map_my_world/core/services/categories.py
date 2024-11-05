from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from map_my_world.core.services.generic import GenericService
from map_my_world.shared.adapters.db.sql.models import Categories
from map_my_world.core.schemas.categories import CategoryCreateSchema, CategoryReadSchema


class CategoryService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.generic_service = GenericService(session)

    async def get_category_by_id(self, category_id: UUID) -> Categories:
        result = await self.generic_service.get_by_primary_key(key=category_id, model=Categories)
        return result

    async def list(self, limit: int = 10, offset: int = 0, categories_filter: object = None) -> list[Categories]:
        statement = select(Categories)
        if categories_filter:
            statement = categories_filter.filter(statement)
        statement = statement.offset(offset)
        statement = statement.limit(limit)
        results = await self.session.exec(statement)
        return results.all()

    async def create(self, category_create: CategoryCreateSchema) -> CategoryReadSchema:
        category = Categories(**category_create.dict())
        self.session.add(category)
        await self.session.commit()
        return category
