from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()


group_table = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(150), unique=True),
)

user_to_groups_table = Table(
    "user_to_groups",
    Column("user_id", Integer, ForeignKey("users")),
    Column("group_id", Integer, ForeignKey("groups")),
)
