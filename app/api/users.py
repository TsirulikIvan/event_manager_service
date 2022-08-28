from typing import Any

from fastapi import APIRouter

from app.models.database import database
from app.models.users import users_table

router = APIRouter(tags=["users - API"])

router.get("/", summary="Get user list")


async def get_users_list() -> list[Any]:
    return await database.fetch_all(users_table.select())
