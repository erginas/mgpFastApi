from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2023_09 import DepoSayimi202309, DepoSayimi202309Create
from models.depo_sayimi_2023_09 import DepoSayimi202309 as DBDepoSayimi202309
from crud.depo_sayimi_2023_09 import get_all_depo_sayimi_2023_09, get_depo_sayimi_2023_09_by_id, create_depo_sayimi_2023_09

router = APIRouter(prefix='/depo_sayimi_2023_09', tags=['DepoSayimi202309'])

@router.get('/', response_model=list[DepoSayimi202309])
async def list_depo_sayimi_2023_09(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2023_09(db)

@router.get('/{id}', response_model=DepoSayimi202309)
async def get_depo_sayimi_2023_09_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2023_09_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi202309)
async def create_depo_sayimi_2023_09_item(data: DepoSayimi202309Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi202309(**data.dict())
    return await create_depo_sayimi_2023_09(db, db_item)