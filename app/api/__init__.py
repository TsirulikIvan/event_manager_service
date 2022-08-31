from fastapi import APIRouter

from app.api import equipment, users

router = APIRouter(tags=["Service - API"])

router.include_router(users.router, prefix="/users")
router.include_router(equipment.router, prefix="/equipment")


@router.get("/")
async def health_check():
    return {"Hello": "World"}
