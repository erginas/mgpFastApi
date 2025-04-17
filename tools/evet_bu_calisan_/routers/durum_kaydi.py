from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.durum_kaydi import DurumKaydi, DurumKaydiCreate
from models.durum_kaydi import DurumKaydi as DBDurumKaydi
from crud.durum_kaydi import get_all_durum_kaydi, get_durum_kaydi_by_id, create_durum_kaydi

router = APIRouter(prefix='/durum_kaydi', tags=['DurumKaydi'])

@router.get('/', response_model=list[DurumKaydi])
async def list_durum_kaydi(db: AsyncSession = Depends()):
    return await get_all_durum_kaydi(db)

@router.get('/{id}', response_model=DurumKaydi)
async def get_durum_kaydi_item(id: int, db: AsyncSession = Depends()):
    result = await get_durum_kaydi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DurumKaydi)
async def create_durum_kaydi_item(data: DurumKaydiCreate, db: AsyncSession = Depends()):
    db_item = DBDurumKaydi(**data.dict())
    return await create_durum_kaydi(db, db_item)