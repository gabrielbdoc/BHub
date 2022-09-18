from fastapi import APIRouter

from src.routers import user_api, banking_api, image
from src.settings import BASE_PATH

api_router = APIRouter(prefix=BASE_PATH)
api_router.include_router(user_api.router)
api_router.include_router(banking_api.router)
api_router.include_router(image.router)
