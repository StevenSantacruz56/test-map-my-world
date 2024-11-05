from uuid import UUID

from fastapi import (APIRouter, status, Body, Depends)

from map_my_world.core.services.categories import CategoryService
from map_my_world.dependencies.repositories import get_repository
from map_my_world.core.schemas.categories import CategoryReadSchema, CategoryCreateSchema
from map_my_world.core.filters.categories import CategoriesFilter

router = APIRouter()


@router.get(
    "",
    response_model=list[CategoryReadSchema],
    status_code=status.HTTP_200_OK,
    name="get_categories",
)
async def get_categories(limit: int = 10, offset: int = 0,
                         repository: CategoryService = Depends(get_repository(CategoryService)),
                         categories_filter: CategoriesFilter = Depends(CategoriesFilter)):
    return await repository.list(limit=limit, offset=offset, categories_filter=categories_filter)


@router.get(
    "/{category_id}",
    response_model=CategoryReadSchema,
    status_code=status.HTTP_200_OK,
    name="get_category",
)
async def get_category_id(category_id: UUID,
                          repository: CategoryService = Depends(get_repository(CategoryService))):
    return await repository.get_category_by_id(category_id=category_id)


@router.post(
    "",
    response_model=CategoryReadSchema,
    status_code=status.HTTP_201_CREATED,
    name="create_location",
)
async def create_category(
        category_create: CategoryCreateSchema = Body(...),
        repository: CategoryService = Depends(get_repository(CategoryService)),
) -> CategoryReadSchema:
    return await repository.create(category_create=category_create)
