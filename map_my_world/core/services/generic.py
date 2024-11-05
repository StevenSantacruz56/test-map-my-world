from typing import (Any, TypeVar, Type)
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from map_my_world.shared.adapters.db.sql.errors import EntityDoesNotExist


T = TypeVar('T', bound=SQLModel)


class GenericService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_primary_key(self, key: Any, model: Type[T], wheres: list = [], model_name: str = None):
        statement = (
            select(model)
            .where(model.__mapper__.primary_key[0] == key, *wheres)
        )
        result = await self.session.exec(statement)
        result = result.first()
        if result is None:
            raise EntityDoesNotExist(message=f'{key} in {model_name or model.__name__} does not exist')
        return result

    async def get(self, model: Type[T] | list[SQLModel], wheres: list, raise_exception: bool = True, joins: list[
        SQLModel | tuple[SQLModel, bool]
    ] = None) -> T:
        if not wheres:
            raise ValueError('wheres is required')
        statement = (
            select(*model) if isinstance(model, list) else select(model)
        )
        if joins:
            for join in joins:
                if isinstance(join, tuple) and len(join) == 3:
                    statement = statement.join(join[0], onclause=join[1], isouter=join[2])
                else:
                    statement = statement.join(join)
        statement = statement.where(*wheres)
        result = await self.session.exec(statement)
        result = result.first()
        if result is None and raise_exception:
            print([where.__dict__ for where in wheres])
            if isinstance(model, list) and model:
                raise EntityDoesNotExist(message=f'{model[0].__name__} does not exist')
            raise EntityDoesNotExist(message=f'{model.__name__} does not exist')
        return result

    async def get_all(self, model: Type[T], wheres: list = [], joins: list = [],
                      order_by: list = None) -> list[T]:
        statement = (
            select(model)
        )
        for join in joins:
            statement = statement.join(join)
        if wheres:
            statement = statement.where(*wheres)
        if order_by:
            statement = statement.order_by(*order_by)
        result = await self.session.exec(statement)
        return result.all()
