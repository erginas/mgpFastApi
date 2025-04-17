from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.temin_sekli import TeminSekli, TeminSekliCreate
from models.temin_sekli import TeminSekli as DBTeminSekli
from crud.temin_sekli import get_all_temin_sekli, get_temin_sekli_by_id, create_temin_sekli

router = APIRouter(prefix='/temin_sekli', tags=['TeminSekli'])

@router.get('/', response_model=list[TeminSekli])
async def list_temin_sekli(db: AsyncSession = Depends()):
    return await get_all_temin_sekli(db)

@router.get('/{id}', response_model=TeminSekli)
async def get_temin_sekli_item(id: int, db: AsyncSession = Depends()):
    result = await get_temin_sekli_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TeminSekli)
async def create_temin_sekli_item(data: TeminSekliCreate, db: AsyncSession = Depends()):
    db_item = DBTeminSekli(**data.dict())
    return await create_temin_sekli(db, db_item)