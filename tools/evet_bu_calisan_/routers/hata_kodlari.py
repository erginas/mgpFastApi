from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.hata_kodlari import HataKodlari, HataKodlariCreate
from models.hata_kodlari import HataKodlari as DBHataKodlari
from crud.hata_kodlari import get_all_hata_kodlari, get_hata_kodlari_by_id, create_hata_kodlari

router = APIRouter(prefix='/hata_kodlari', tags=['HataKodlari'])

@router.get('/', response_model=list[HataKodlari])
async def list_hata_kodlari(db: AsyncSession = Depends()):
    return await get_all_hata_kodlari(db)

@router.get('/{id}', response_model=HataKodlari)
async def get_hata_kodlari_item(id: int, db: AsyncSession = Depends()):
    result = await get_hata_kodlari_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=HataKodlari)
async def create_hata_kodlari_item(data: HataKodlariCreate, db: AsyncSession = Depends()):
    db_item = DBHataKodlari(**data.dict())
    return await create_hata_kodlari(db, db_item)