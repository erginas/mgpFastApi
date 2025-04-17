from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ubb_fiyat import UbbFiyat, UbbFiyatCreate
from models.ubb_fiyat import UbbFiyat as DBUbbFiyat
from crud.ubb_fiyat import get_all_ubb_fiyat, get_ubb_fiyat_by_id, create_ubb_fiyat

router = APIRouter(prefix='/ubb_fiyat', tags=['UbbFiyat'])

@router.get('/', response_model=list[UbbFiyat])
async def list_ubb_fiyat(db: AsyncSession = Depends()):
    return await get_all_ubb_fiyat(db)

@router.get('/{id}', response_model=UbbFiyat)
async def get_ubb_fiyat_item(id: int, db: AsyncSession = Depends()):
    result = await get_ubb_fiyat_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UbbFiyat)
async def create_ubb_fiyat_item(data: UbbFiyatCreate, db: AsyncSession = Depends()):
    db_item = DBUbbFiyat(**data.dict())
    return await create_ubb_fiyat(db, db_item)