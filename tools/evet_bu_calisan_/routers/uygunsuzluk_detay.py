from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk_detay import UygunsuzlukDetay, UygunsuzlukDetayCreate
from models.uygunsuzluk_detay import UygunsuzlukDetay as DBUygunsuzlukDetay
from crud.uygunsuzluk_detay import get_all_uygunsuzluk_detay, get_uygunsuzluk_detay_by_id, create_uygunsuzluk_detay

router = APIRouter(prefix='/uygunsuzluk_detay', tags=['UygunsuzlukDetay'])

@router.get('/', response_model=list[UygunsuzlukDetay])
async def list_uygunsuzluk_detay(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk_detay(db)

@router.get('/{id}', response_model=UygunsuzlukDetay)
async def get_uygunsuzluk_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygunsuzlukDetay)
async def create_uygunsuzluk_detay_item(data: UygunsuzlukDetayCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzlukDetay(**data.dict())
    return await create_uygunsuzluk_detay(db, db_item)