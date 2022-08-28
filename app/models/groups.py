from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


groups_table = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(150), unique=True),
)
