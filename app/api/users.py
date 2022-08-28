import hashlib
import random
import string
from http import HTTPStatus

from asyncpg.exceptions import NoDataFoundError, UniqueViolationError
from fastapi import APIRouter, HTTPException

from app.models.database import database
from app.models.users import UserRole, users_table
from app.schemas.users import (CreateUserRequest, UpdateUserRequest,
                               UserResponse)

router = APIRouter()


def get_random_string(length=12):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(password: str, salt: str = None):
    if salt is None:
        salt = get_random_string()
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


@router.get("/", summary="Get user list")
async def get_users_list() -> list[UserResponse]:
    return [
        UserResponse(**user)
        for user in (await database.fetch_all(users_table.select()))
    ]


@router.post("/create", summary="Create user at DB")
async def crete_user(payload: CreateUserRequest) -> UserResponse:
    password_hash = hash_password(payload.password)
    payload.password = password_hash
    role = UserRole.common
    query = users_table.insert().values(**payload.dict(), role=role)

    try:
        response = await database.execute(query)
    except UniqueViolationError as e:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=str(e))

    return UserResponse(**payload.dict(), id=response, role=role)


@router.get("/{user_id}", summary="Get user by id")
async def get_user_by_id(user_id: int) -> UserResponse:
    response = await database.fetch_one(
        users_table.select().where(users_table.c.id == user_id)
    )

    if response:
        return UserResponse(**response)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")


@router.put("/{user_id}", summary="Update user data at DB")
async def update_user(user_id: int, update_params: UpdateUserRequest) -> None:
    query = (
        users_table.update()
        .where(users_table.c.id == user_id)
        .values(**update_params.dict())
    )
    try:
        response = await database.execute(query)
    except NoDataFoundError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(e))

    return response
