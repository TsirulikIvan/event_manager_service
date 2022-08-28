from pydantic import BaseModel, EmailStr

from app.models.users import UserRole


class CreateUserRequest(BaseModel):
    name: str
    surname: str
    email: EmailStr
    vk_link: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    role: UserRole
    vk_link: str


class UpdateUserRequest(BaseModel):
    email: EmailStr | None
    vk_link: str | None
