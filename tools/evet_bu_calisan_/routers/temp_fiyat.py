from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.temp_fiyat import TempFiyat, TempFiyatCreate
from models.temp_fiyat import TempFiyat as DBTempFiyat
from crud.temp_fiyat import get_all_temp_fiyat, get_temp_fiyat_by_id, create_temp_fiyat

router = APIRouter(prefix='/temp_fiyat', tags=['TempFiyat'])

@router.get('/', response_model=list[TempFiyat])
async def list_temp_fiyat(db: AsyncSession = Depends()):
    return await get_all_temp_fiyat(db)

@router.get('/{id}', response_model=TempFiyat)
async def get_temp_fiyat_item(id: int, db: AsyncSession = Depends()):
    result = await get_temp_fiyat_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TempFiyat)
async def create_temp_fiyat_item(data: TempFiyatCreate, db: AsyncSession = Depends()):
    db_item = DBTempFiyat(**data.dict())
    return await create_temp_fiyat(db, db_item)