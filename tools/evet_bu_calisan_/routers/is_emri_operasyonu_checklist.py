from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_operasyonu_checklist import IsEmriOperasyonuChecklist, IsEmriOperasyonuChecklistCreate
from models.is_emri_operasyonu_checklist import IsEmriOperasyonuChecklist as DBIsEmriOperasyonuChecklist
from crud.is_emri_operasyonu_checklist import get_all_is_emri_operasyonu_checklist, get_is_emri_operasyonu_checklist_by_id, create_is_emri_operasyonu_checklist

router = APIRouter(prefix='/is_emri_operasyonu_checklist', tags=['IsEmriOperasyonuChecklist'])

@router.get('/', response_model=list[IsEmriOperasyonuChecklist])
async def list_is_emri_operasyonu_checklist(db: AsyncSession = Depends()):
    return await get_all_is_emri_operasyonu_checklist(db)

@router.get('/{id}', response_model=IsEmriOperasyonuChecklist)
async def get_is_emri_operasyonu_checklist_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_operasyonu_checklist_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriOperasyonuChecklist)
async def create_is_emri_operasyonu_checklist_item(data: IsEmriOperasyonuChecklistCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriOperasyonuChecklist(**data.dict())
    return await create_is_emri_operasyonu_checklist(db, db_item)