from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.gecici_stok_detay import GeciciStokDetay, GeciciStokDetayCreate
from models.gecici_stok_detay import GeciciStokDetay as DBGeciciStokDetay
from crud.gecici_stok_detay import get_all_gecici_stok_detay, get_gecici_stok_detay_by_id, create_gecici_stok_detay

router = APIRouter(prefix='/gecici_stok_detay', tags=['GeciciStokDetay'])

@router.get('/', response_model=list[GeciciStokDetay])
async def list_gecici_stok_detay(db: AsyncSession = Depends()):
    return await get_all_gecici_stok_detay(db)

@router.get('/{id}', response_model=GeciciStokDetay)
async def get_gecici_stok_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_gecici_stok_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=GeciciStokDetay)
async def create_gecici_stok_detay_item(data: GeciciStokDetayCreate, db: AsyncSession = Depends()):
    db_item = DBGeciciStokDetay(**data.dict())
    return await create_gecici_stok_detay(db, db_item)