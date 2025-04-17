from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2010_01 import DepoSayimi201001, DepoSayimi201001Create
from models.depo_sayimi_2010_01 import DepoSayimi201001 as DBDepoSayimi201001
from crud.depo_sayimi_2010_01 import get_all_depo_sayimi_2010_01, get_depo_sayimi_2010_01_by_id, create_depo_sayimi_2010_01

router = APIRouter(prefix='/depo_sayimi_2010_01', tags=['DepoSayimi201001'])

@router.get('/', response_model=list[DepoSayimi201001])
async def list_depo_sayimi_2010_01(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2010_01(db)

@router.get('/{id}', response_model=DepoSayimi201001)
async def get_depo_sayimi_2010_01_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2010_01_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi201001)
async def create_depo_sayimi_2010_01_item(data: DepoSayimi201001Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi201001(**data.dict())
    return await create_depo_sayimi_2010_01(db, db_item)