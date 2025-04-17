from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.giris_kalite_detay import GirisKaliteDetay, GirisKaliteDetayCreate
from models.giris_kalite_detay import GirisKaliteDetay as DBGirisKaliteDetay
from crud.giris_kalite_detay import get_all_giris_kalite_detay, get_giris_kalite_detay_by_id, create_giris_kalite_detay

router = APIRouter(prefix='/giris_kalite_detay', tags=['GirisKaliteDetay'])

@router.get('/', response_model=list[GirisKaliteDetay])
async def list_giris_kalite_detay(db: AsyncSession = Depends()):
    return await get_all_giris_kalite_detay(db)

@router.get('/{id}', response_model=GirisKaliteDetay)
async def get_giris_kalite_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_giris_kalite_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=GirisKaliteDetay)
async def create_giris_kalite_detay_item(data: GirisKaliteDetayCreate, db: AsyncSession = Depends()):
    db_item = DBGirisKaliteDetay(**data.dict())
    return await create_giris_kalite_detay(db, db_item)