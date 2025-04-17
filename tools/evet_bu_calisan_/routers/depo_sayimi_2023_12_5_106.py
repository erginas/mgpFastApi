from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2023_12_5_106 import DepoSayimi2023125106, DepoSayimi2023125106Create
from models.depo_sayimi_2023_12_5_106 import DepoSayimi2023125106 as DBDepoSayimi2023125106
from crud.depo_sayimi_2023_12_5_106 import get_all_depo_sayimi_2023_12_5_106, get_depo_sayimi_2023_12_5_106_by_id, create_depo_sayimi_2023_12_5_106

router = APIRouter(prefix='/depo_sayimi_2023_12_5_106', tags=['DepoSayimi2023125106'])

@router.get('/', response_model=list[DepoSayimi2023125106])
async def list_depo_sayimi_2023_12_5_106(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2023_12_5_106(db)

@router.get('/{id}', response_model=DepoSayimi2023125106)
async def get_depo_sayimi_2023_12_5_106_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2023_12_5_106_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi2023125106)
async def create_depo_sayimi_2023_12_5_106_item(data: DepoSayimi2023125106Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi2023125106(**data.dict())
    return await create_depo_sayimi_2023_12_5_106(db, db_item)