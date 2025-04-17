from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygunsuzluk_gorus_bildiren import UygunsuzlukGorusBildiren, UygunsuzlukGorusBildirenCreate
from models.uygunsuzluk_gorus_bildiren import UygunsuzlukGorusBildiren as DBUygunsuzlukGorusBildiren
from crud.uygunsuzluk_gorus_bildiren import get_all_uygunsuzluk_gorus_bildiren, get_uygunsuzluk_gorus_bildiren_by_id, create_uygunsuzluk_gorus_bildiren

router = APIRouter(prefix='/uygunsuzluk_gorus_bildiren', tags=['UygunsuzlukGorusBildiren'])

@router.get('/', response_model=list[UygunsuzlukGorusBildiren])
async def list_uygunsuzluk_gorus_bildiren(db: AsyncSession = Depends()):
    return await get_all_uygunsuzluk_gorus_bildiren(db)

@router.get('/{id}', response_model=UygunsuzlukGorusBildiren)
async def get_uygunsuzluk_gorus_bildiren_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygunsuzluk_gorus_bildiren_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygunsuzlukGorusBildiren)
async def create_uygunsuzluk_gorus_bildiren_item(data: UygunsuzlukGorusBildirenCreate, db: AsyncSession = Depends()):
    db_item = DBUygunsuzlukGorusBildiren(**data.dict())
    return await create_uygunsuzluk_gorus_bildiren(db, db_item)