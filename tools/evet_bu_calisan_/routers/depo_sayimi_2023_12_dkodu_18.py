from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2023_12_dkodu_18 import DepoSayimi202312Dkodu18, DepoSayimi202312Dkodu18Create
from models.depo_sayimi_2023_12_dkodu_18 import DepoSayimi202312Dkodu18 as DBDepoSayimi202312Dkodu18
from crud.depo_sayimi_2023_12_dkodu_18 import get_all_depo_sayimi_2023_12_dkodu_18, get_depo_sayimi_2023_12_dkodu_18_by_id, create_depo_sayimi_2023_12_dkodu_18

router = APIRouter(prefix='/depo_sayimi_2023_12_dkodu_18', tags=['DepoSayimi202312Dkodu18'])

@router.get('/', response_model=list[DepoSayimi202312Dkodu18])
async def list_depo_sayimi_2023_12_dkodu_18(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2023_12_dkodu_18(db)

@router.get('/{id}', response_model=DepoSayimi202312Dkodu18)
async def get_depo_sayimi_2023_12_dkodu_18_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2023_12_dkodu_18_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi202312Dkodu18)
async def create_depo_sayimi_2023_12_dkodu_18_item(data: DepoSayimi202312Dkodu18Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi202312Dkodu18(**data.dict())
    return await create_depo_sayimi_2023_12_dkodu_18(db, db_item)