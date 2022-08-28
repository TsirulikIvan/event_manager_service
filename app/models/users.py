import enum

from sqlalchemy import Column, Enum, Integer, MetaData, String, Table


class UserRole(enum.Enum):
    common = 1
    admin = 2
    supervisor = 3


metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(100), nullable=False),
    Column("surname", String(100), nullable=False),
    Column("email", String(50), unique=True, index=True),
    Column("vk_link", String(150), unique=True),
    Column("password", String()),
    Column("role", Enum(UserRole)),
)
