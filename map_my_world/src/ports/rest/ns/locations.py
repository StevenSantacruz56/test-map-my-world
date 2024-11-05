from uuid import UUID

from fastapi import (APIRouter, status, Body, Depends)

from map_my_world.core.services.locations import LocationsService
from map_my_world.dependencies.repositories import get_repository
from map_my_world.core.schemas.locations import LocationCreateSchema, LocationReadSchema
from map_my_world.core.filters.locations import LocationsFilter

router = APIRouter()


@router.get(
    "",
    response_model=list[LocationReadSchema],
    status_code=status.HTTP_200_OK,
    name="get_locations",
)
async def get_categories(limit: int = 10, offset: int = 0,
                         repository: LocationsService = Depends(get_repository(LocationsService)),
                         location_filter: LocationsFilter = Depends(LocationsFilter)):
    return await repository.list(limit=limit, offset=offset, location_filter=location_filter)


@router.get(
    "/{location_id}",
    response_model=LocationReadSchema,
    status_code=status.HTTP_200_OK,
    name="get_location",
)
async def get_location_id(location_id: UUID,
                          repository: LocationsService = Depends(get_repository(LocationsService))):
    return await repository.get_location_by_id(location_id=location_id)


@router.post(
    "",
    response_model=LocationReadSchema,
    status_code=status.HTTP_201_CREATED,
    name="create_location",
)
async def create_location(
        location_create: LocationCreateSchema = Body(...),
        repository: LocationsService = Depends(get_repository(LocationsService)),
) -> LocationReadSchema:
    return await repository.create(location_create=location_create)
