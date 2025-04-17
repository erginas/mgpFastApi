from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_temin_yeri import MalzemeTeminYeri, MalzemeTeminYeriCreate
from models.malzeme_temin_yeri import MalzemeTeminYeri as DBMalzemeTeminYeri
from crud.malzeme_temin_yeri import get_all_malzeme_temin_yeri, get_malzeme_temin_yeri_by_id, create_malzeme_temin_yeri

router = APIRouter(prefix='/malzeme_temin_yeri', tags=['MalzemeTeminYeri'])

@router.get('/', response_model=list[MalzemeTeminYeri])
async def list_malzeme_temin_yeri(db: AsyncSession = Depends()):
    return await get_all_malzeme_temin_yeri(db)

@router.get('/{id}', response_model=MalzemeTeminYeri)
async def get_malzeme_temin_yeri_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_temin_yeri_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeTeminYeri)
async def create_malzeme_temin_yeri_item(data: MalzemeTeminYeriCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeTeminYeri(**data.dict())
    return await create_malzeme_temin_yeri(db, db_item)