from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2004_07 import DepoSayimi200407, DepoSayimi200407Create
from models.depo_sayimi_2004_07 import DepoSayimi200407 as DBDepoSayimi200407
from crud.depo_sayimi_2004_07 import get_all_depo_sayimi_2004_07, get_depo_sayimi_2004_07_by_id, create_depo_sayimi_2004_07

router = APIRouter(prefix='/depo_sayimi_2004_07', tags=['DepoSayimi200407'])

@router.get('/', response_model=list[DepoSayimi200407])
async def list_depo_sayimi_2004_07(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2004_07(db)

@router.get('/{id}', response_model=DepoSayimi200407)
async def get_depo_sayimi_2004_07_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2004_07_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi200407)
async def create_depo_sayimi_2004_07_item(data: DepoSayimi200407Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi200407(**data.dict())
    return await create_depo_sayimi_2004_07(db, db_item)