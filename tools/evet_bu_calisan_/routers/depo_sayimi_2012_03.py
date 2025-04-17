from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2012_03 import DepoSayimi201203, DepoSayimi201203Create
from models.depo_sayimi_2012_03 import DepoSayimi201203 as DBDepoSayimi201203
from crud.depo_sayimi_2012_03 import get_all_depo_sayimi_2012_03, get_depo_sayimi_2012_03_by_id, create_depo_sayimi_2012_03

router = APIRouter(prefix='/depo_sayimi_2012_03', tags=['DepoSayimi201203'])

@router.get('/', response_model=list[DepoSayimi201203])
async def list_depo_sayimi_2012_03(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2012_03(db)

@router.get('/{id}', response_model=DepoSayimi201203)
async def get_depo_sayimi_2012_03_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2012_03_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi201203)
async def create_depo_sayimi_2012_03_item(data: DepoSayimi201203Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi201203(**data.dict())
    return await create_depo_sayimi_2012_03(db, db_item)