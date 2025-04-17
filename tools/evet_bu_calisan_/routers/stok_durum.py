from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.stok_durum import StokDurum, StokDurumCreate
from models.stok_durum import StokDurum as DBStokDurum
from crud.stok_durum import get_all_stok_durum, get_stok_durum_by_id, create_stok_durum

router = APIRouter(prefix='/stok_durum', tags=['StokDurum'])

@router.get('/', response_model=list[StokDurum])
async def list_stok_durum(db: AsyncSession = Depends()):
    return await get_all_stok_durum(db)

@router.get('/{id}', response_model=StokDurum)
async def get_stok_durum_item(id: int, db: AsyncSession = Depends()):
    result = await get_stok_durum_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=StokDurum)
async def create_stok_durum_item(data: StokDurumCreate, db: AsyncSession = Depends()):
    db_item = DBStokDurum(**data.dict())
    return await create_stok_durum(db, db_item)