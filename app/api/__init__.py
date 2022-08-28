from fastapi import APIRouter

from app.api import users

router = APIRouter(tags=["Service - API"])

router.include_router(users.router, prefix="/users")
