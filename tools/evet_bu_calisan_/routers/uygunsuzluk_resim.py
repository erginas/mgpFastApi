from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk_resim import UygunsuzlukResim, UygunsuzlukResimCreate
from models.uygunsuzluk_resim import UygunsuzlukResim as DBUygunsuzlukResim
from crud.uygunsuzluk_resim import get_all_uygunsuzluk_resim, get_uygunsuzluk_resim_by_id, create_uygunsuzluk_resim

router = APIRouter(prefix='/uygunsuzluk_resim', tags=['UygunsuzlukResim'])

@router.get('/', response_model=list[UygunsuzlukResim])
async def list_uygunsuzluk_resim(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk_resim(db)

@router.get('/{id}', response_model=UygunsuzlukResim)
async def get_uygunsuzluk_resim_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_resim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygunsuzlukResim)
async def create_uygunsuzluk_resim_item(data: UygunsuzlukResimCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzlukResim(**data.dict())
    return await create_uygunsuzluk_resim(db, db_item)