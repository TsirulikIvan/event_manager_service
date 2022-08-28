import enum

from sqlalchemy import Column, Enum, Integer, MetaData, String, Table, ForeignKey
from app.models.users import users_table


class EquipmentClass(enum.Enum):
    tent = 1
    sleeping_bag = 2
    tourist_foam = 3


metadata = MetaData()


equipment_table = Table(
    "equipment",
    metadata,
    Column("user_id", Integer, ForeignKey(users_table.c.id)),
    Column("name", String(100), nullable=False),
    Column("class", Enum(EquipmentClass)),
)
