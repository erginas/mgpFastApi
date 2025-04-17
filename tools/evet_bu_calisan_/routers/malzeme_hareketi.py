from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_hareketi import MalzemeHareketi, MalzemeHareketiCreate
from models.malzeme_hareketi import MalzemeHareketi as DBMalzemeHareketi
from crud.malzeme_hareketi import get_all_malzeme_hareketi, get_malzeme_hareketi_by_id, create_malzeme_hareketi

router = APIRouter(prefix='/malzeme_hareketi', tags=['MalzemeHareketi'])

@router.get('/', response_model=list[MalzemeHareketi])
async def list_malzeme_hareketi(db: AsyncSession = Depends()):
    return await get_all_malzeme_hareketi(db)

@router.get('/{id}', response_model=MalzemeHareketi)
async def get_malzeme_hareketi_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_hareketi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeHareketi)
async def create_malzeme_hareketi_item(data: MalzemeHareketiCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeHareketi(**data.dict())
    return await create_malzeme_hareketi(db, db_item)