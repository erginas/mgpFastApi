from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2023_12_v1 import DepoSayimi202312V1, DepoSayimi202312V1Create
from models.depo_sayimi_2023_12_v1 import DepoSayimi202312V1 as DBDepoSayimi202312V1
from crud.depo_sayimi_2023_12_v1 import get_all_depo_sayimi_2023_12_v1, get_depo_sayimi_2023_12_v1_by_id, create_depo_sayimi_2023_12_v1

router = APIRouter(prefix='/depo_sayimi_2023_12_v1', tags=['DepoSayimi202312V1'])

@router.get('/', response_model=list[DepoSayimi202312V1])
async def list_depo_sayimi_2023_12_v1(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2023_12_v1(db)

@router.get('/{id}', response_model=DepoSayimi202312V1)
async def get_depo_sayimi_2023_12_v1_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2023_12_v1_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi202312V1)
async def create_depo_sayimi_2023_12_v1_item(data: DepoSayimi202312V1Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi202312V1(**data.dict())
    return await create_depo_sayimi_2023_12_v1(db, db_item)