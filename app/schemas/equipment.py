from pydantic import BaseModel

from app.models.equipment import EquipmentClass


class CreateEquipmentRequest(BaseModel):
    name: str
    eq_class: EquipmentClass


class EquipmentResponse(CreateEquipmentRequest):
    user_id: int
