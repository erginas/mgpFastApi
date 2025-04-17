from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk import Uygunsuzluk, UygunsuzlukCreate
from models.uygunsuzluk import Uygunsuzluk as DBUygunsuzluk
from crud.uygunsuzluk import get_all_uygunsuzluk, get_uygunsuzluk_by_id, create_uygunsuzluk

router = APIRouter(prefix='/uygunsuzluk', tags=['Uygunsuzluk'])

@router.get('/', response_model=list[Uygunsuzluk])
async def list_uygunsuzluk(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk(db)

@router.get('/{id}', response_model=Uygunsuzluk)
async def get_uygunsuzluk_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Uygunsuzluk)
async def create_uygunsuzluk_item(data: UygunsuzlukCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzluk(**data.dict())
    return await create_uygunsuzluk(db, db_item)