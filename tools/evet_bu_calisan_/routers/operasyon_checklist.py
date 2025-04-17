from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.operasyon_checklist import OperasyonChecklist, OperasyonChecklistCreate
from models.operasyon_checklist import OperasyonChecklist as DBOperasyonChecklist
from crud.operasyon_checklist import get_all_operasyon_checklist, get_operasyon_checklist_by_id, create_operasyon_checklist

router = APIRouter(prefix='/operasyon_checklist', tags=['OperasyonChecklist'])

@router.get('/', response_model=list[OperasyonChecklist])
async def list_operasyon_checklist(db: AsyncSession = Depends()):
    return await get_all_operasyon_checklist(db)

@router.get('/{id}', response_model=OperasyonChecklist)
async def get_operasyon_checklist_item(id: int, db: AsyncSession = Depends()):
    result = await get_operasyon_checklist_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=OperasyonChecklist)
async def create_operasyon_checklist_item(data: OperasyonChecklistCreate, db: AsyncSession = Depends()):
    db_item = DBOperasyonChecklist(**data.dict())
    return await create_operasyon_checklist(db, db_item)