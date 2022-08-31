from fastapi import APIRouter, HTTPException, status
from app.models.database import database
from app.models.equipment import equipment_table
from app.schemas.equipment import CreateEquipmentRequest, EquipmentResponse


router = APIRouter(tags=["equipment - API"])


@router.get("")
async def get_equipment() -> list[EquipmentResponse]:
    response = await database.fetch_all(equipment_table.select())

    return [EquipmentResponse(**item) for item in response]


@router.post("/create")
async def add_equipment(payload: CreateEquipmentRequest) -> int:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)