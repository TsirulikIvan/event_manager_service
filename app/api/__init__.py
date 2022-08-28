from fastapi import APIRouter

from app.api import users

router = APIRouter(tags=["Service - API"])

router.include_router(users.router, prefix="/users")


@router.get("/")
async def health_check():
    return {"Hello": "World"}
