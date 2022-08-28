from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table

from app.models.groups import groups_table
from app.models.users import users_table

metadata = MetaData()

users_to_groups_table = Table(
    "users_to_groups",
    metadata,
    Column("user_id", Integer, ForeignKey(users_table.c.id)),
    Column("group_id", Integer, ForeignKey(groups_table.c.id)),
)
