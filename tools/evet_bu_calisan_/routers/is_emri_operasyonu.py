from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_operasyonu import IsEmriOperasyonu, IsEmriOperasyonuCreate
from models.is_emri_operasyonu import IsEmriOperasyonu as DBIsEmriOperasyonu
from crud.is_emri_operasyonu import get_all_is_emri_operasyonu, get_is_emri_operasyonu_by_id, create_is_emri_operasyonu

router = APIRouter(prefix='/is_emri_operasyonu', tags=['IsEmriOperasyonu'])

@router.get('/', response_model=list[IsEmriOperasyonu])
async def list_is_emri_operasyonu(db: AsyncSession = Depends()):
    return await get_all_is_emri_operasyonu(db)

@router.get('/{id}', response_model=IsEmriOperasyonu)
async def get_is_emri_operasyonu_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_operasyonu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriOperasyonu)
async def create_is_emri_operasyonu_item(data: IsEmriOperasyonuCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriOperasyonu(**data.dict())
    return await create_is_emri_operasyonu(db, db_item)