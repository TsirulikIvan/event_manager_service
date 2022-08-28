from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()


groups_table = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(150), unique=True),
)

users_to_groups_table = Table(
    "users_to_groups",
    metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("group_id", Integer, ForeignKey("groups.id")),
)
