from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.haberler_makale import HaberlerMakale, HaberlerMakaleCreate
from models.haberler_makale import HaberlerMakale as DBHaberlerMakale
from crud.haberler_makale import get_all_haberler_makale, get_haberler_makale_by_id, create_haberler_makale

router = APIRouter(prefix='/haberler_makale', tags=['HaberlerMakale'])

@router.get('/', response_model=list[HaberlerMakale])
async def list_haberler_makale(db: AsyncSession = Depends()):
    return await get_all_haberler_makale(db)

@router.get('/{id}', response_model=HaberlerMakale)
async def get_haberler_makale_item(id: int, db: AsyncSession = Depends()):
    result = await get_haberler_makale_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=HaberlerMakale)
async def create_haberler_makale_item(data: HaberlerMakaleCreate, db: AsyncSession = Depends()):
    db_item = DBHaberlerMakale(**data.dict())
    return await create_haberler_makale(db, db_item)