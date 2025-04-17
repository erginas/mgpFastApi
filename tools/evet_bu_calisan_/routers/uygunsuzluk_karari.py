from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk_karari import UygunsuzlukKarari, UygunsuzlukKarariCreate
from models.uygunsuzluk_karari import UygunsuzlukKarari as DBUygunsuzlukKarari
from crud.uygunsuzluk_karari import get_all_uygunsuzluk_karari, get_uygunsuzluk_karari_by_id, create_uygunsuzluk_karari

router = APIRouter(prefix='/uygunsuzluk_karari', tags=['UygunsuzlukKarari'])

@router.get('/', response_model=list[UygunsuzlukKarari])
async def list_uygunsuzluk_karari(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk_karari(db)

@router.get('/{id}', response_model=UygunsuzlukKarari)
async def get_uygunsuzluk_karari_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_karari_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygunsuzlukKarari)
async def create_uygunsuzluk_karari_item(data: UygunsuzlukKarariCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzlukKarari(**data.dict())
    return await create_uygunsuzluk_karari(db, db_item)