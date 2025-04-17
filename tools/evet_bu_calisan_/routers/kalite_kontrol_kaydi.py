from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kalite_kontrol_kaydi import KaliteKontrolKaydi, KaliteKontrolKaydiCreate
from models.kalite_kontrol_kaydi import KaliteKontrolKaydi as DBKaliteKontrolKaydi
from crud.kalite_kontrol_kaydi import get_all_kalite_kontrol_kaydi, get_kalite_kontrol_kaydi_by_id, create_kalite_kontrol_kaydi

router = APIRouter(prefix='/kalite_kontrol_kaydi', tags=['KaliteKontrolKaydi'])

@router.get('/', response_model=list[KaliteKontrolKaydi])
async def list_kalite_kontrol_kaydi(db: AsyncSession = Depends()):
    return await get_all_kalite_kontrol_kaydi(db)

@router.get('/{id}', response_model=KaliteKontrolKaydi)
async def get_kalite_kontrol_kaydi_item(id: int, db: AsyncSession = Depends()):
    result = await get_kalite_kontrol_kaydi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KaliteKontrolKaydi)
async def create_kalite_kontrol_kaydi_item(data: KaliteKontrolKaydiCreate, db: AsyncSession = Depends()):
    db_item = DBKaliteKontrolKaydi(**data.dict())
    return await create_kalite_kontrol_kaydi(db, db_item)