from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.catalog import brand_router
from app.api.v1.endpoints.catalog import router as catalog_router
from app.api.v1.endpoints.catalog import product_router
api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(catalog_router)
api_router.include_router(brand_router)
api_router.include_router(product_router)