from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk_sorumlusu import UygunsuzlukSorumlusu, UygunsuzlukSorumlusuCreate
from models.uygunsuzluk_sorumlusu import UygunsuzlukSorumlusu as DBUygunsuzlukSorumlusu
from crud.uygunsuzluk_sorumlusu import get_all_uygunsuzluk_sorumlusu, get_uygunsuzluk_sorumlusu_by_id, create_uygunsuzluk_sorumlusu

router = APIRouter(prefix='/uygunsuzluk_sorumlusu', tags=['UygunsuzlukSorumlusu'])

@router.get('/', response_model=list[UygunsuzlukSorumlusu])
async def list_uygunsuzluk_sorumlusu(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk_sorumlusu(db)

@router.get('/{id}', response_model=UygunsuzlukSorumlusu)
async def get_uygunsuzluk_sorumlusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_sorumlusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygunsuzlukSorumlusu)
async def create_uygunsuzluk_sorumlusu_item(data: UygunsuzlukSorumlusuCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzlukSorumlusu(**data.dict())
    return await create_uygunsuzluk_sorumlusu(db, db_item)