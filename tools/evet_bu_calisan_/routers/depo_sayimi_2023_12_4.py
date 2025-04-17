from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2023_12_4 import DepoSayimi2023124, DepoSayimi2023124Create
from models.depo_sayimi_2023_12_4 import DepoSayimi2023124 as DBDepoSayimi2023124
from crud.depo_sayimi_2023_12_4 import get_all_depo_sayimi_2023_12_4, get_depo_sayimi_2023_12_4_by_id, create_depo_sayimi_2023_12_4

router = APIRouter(prefix='/depo_sayimi_2023_12_4', tags=['DepoSayimi2023124'])

@router.get('/', response_model=list[DepoSayimi2023124])
async def list_depo_sayimi_2023_12_4(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2023_12_4(db)

@router.get('/{id}', response_model=DepoSayimi2023124)
async def get_depo_sayimi_2023_12_4_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2023_12_4_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi2023124)
async def create_depo_sayimi_2023_12_4_item(data: DepoSayimi2023124Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi2023124(**data.dict())
    return await create_depo_sayimi_2023_12_4(db, db_item)