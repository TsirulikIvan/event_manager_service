from sqlalchemy import (TIME, TIMESTAMP, Column, ForeignKey, Integer, MetaData,
                        String, Table)

from app.models.groups import groups_table

metadata = MetaData()


events_table = Table(
    "events",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(150), nullable=False),
    Column("place_name", String(200), nullable=False),
    Column("pred_place_coord", String(100)),
    Column("final_place_coord", String(100)),
    Column("user_group", Integer, ForeignKey(groups_table.c.id)),
    Column("start_datetime", TIMESTAMP),
    Column("duration", TIME),
)
