from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk_gorusu import UygunsuzlukGorusu, UygunsuzlukGorusuCreate
from models.uygunsuzluk_gorusu import UygunsuzlukGorusu as DBUygunsuzlukGorusu
from crud.uygunsuzluk_gorusu import get_all_uygunsuzluk_gorusu, get_uygunsuzluk_gorusu_by_id, create_uygunsuzluk_gorusu

router = APIRouter(prefix='/uygunsuzluk_gorusu', tags=['UygunsuzlukGorusu'])

@router.get('/', response_model=list[UygunsuzlukGorusu])
async def list_uygunsuzluk_gorusu(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk_gorusu(db)

@router.get('/{id}', response_model=UygunsuzlukGorusu)
async def get_uygunsuzluk_gorusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_gorusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygunsuzlukGorusu)
async def create_uygunsuzluk_gorusu_item(data: UygunsuzlukGorusuCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzlukGorusu(**data.dict())
    return await create_uygunsuzluk_gorusu(db, db_item)