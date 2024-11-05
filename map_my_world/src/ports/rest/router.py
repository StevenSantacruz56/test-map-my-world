from fastapi import APIRouter
from map_my_world.src.ports.rest.ns.categories import router as categories_router
from map_my_world.src.ports.rest.ns.locations import router as locations_router

router = APIRouter(prefix="/v1")

router.include_router(categories_router, prefix="/categories")
router.include_router(locations_router, prefix="/locations")
