from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_temin_sekli import MalzemeTeminSekli, MalzemeTeminSekliCreate
from models.malzeme_temin_sekli import MalzemeTeminSekli as DBMalzemeTeminSekli
from crud.malzeme_temin_sekli import get_all_malzeme_temin_sekli, get_malzeme_temin_sekli_by_id, create_malzeme_temin_sekli

router = APIRouter(prefix='/malzeme_temin_sekli', tags=['MalzemeTeminSekli'])

@router.get('/', response_model=list[MalzemeTeminSekli])
async def list_malzeme_temin_sekli(db: AsyncSession = Depends()):
    return await get_all_malzeme_temin_sekli(db)

@router.get('/{id}', response_model=MalzemeTeminSekli)
async def get_malzeme_temin_sekli_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_temin_sekli_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeTeminSekli)
async def create_malzeme_temin_sekli_item(data: MalzemeTeminSekliCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeTeminSekli(**data.dict())
    return await create_malzeme_temin_sekli(db, db_item)