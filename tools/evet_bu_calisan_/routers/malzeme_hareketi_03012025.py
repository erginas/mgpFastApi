from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_hareketi_03012025 import MalzemeHareketi03012025, MalzemeHareketi03012025Create
from models.malzeme_hareketi_03012025 import MalzemeHareketi03012025 as DBMalzemeHareketi03012025
from crud.malzeme_hareketi_03012025 import get_all_malzeme_hareketi_03012025, get_malzeme_hareketi_03012025_by_id, create_malzeme_hareketi_03012025

router = APIRouter(prefix='/malzeme_hareketi_03012025', tags=['MalzemeHareketi03012025'])

@router.get('/', response_model=list[MalzemeHareketi03012025])
async def list_malzeme_hareketi_03012025(db: AsyncSession = Depends()):
    return await get_all_malzeme_hareketi_03012025(db)

@router.get('/{id}', response_model=MalzemeHareketi03012025)
async def get_malzeme_hareketi_03012025_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_hareketi_03012025_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeHareketi03012025)
async def create_malzeme_hareketi_03012025_item(data: MalzemeHareketi03012025Create, db: AsyncSession = Depends()):
    db_item = DBMalzemeHareketi03012025(**data.dict())
    return await create_malzeme_hareketi_03012025(db, db_item)