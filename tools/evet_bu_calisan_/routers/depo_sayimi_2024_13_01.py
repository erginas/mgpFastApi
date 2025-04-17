from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2024_13_01 import DepoSayimi20241301, DepoSayimi20241301Create
from models.depo_sayimi_2024_13_01 import DepoSayimi20241301 as DBDepoSayimi20241301
from crud.depo_sayimi_2024_13_01 import get_all_depo_sayimi_2024_13_01, get_depo_sayimi_2024_13_01_by_id, create_depo_sayimi_2024_13_01

router = APIRouter(prefix='/depo_sayimi_2024_13_01', tags=['DepoSayimi20241301'])

@router.get('/', response_model=list[DepoSayimi20241301])
async def list_depo_sayimi_2024_13_01(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2024_13_01(db)

@router.get('/{id}', response_model=DepoSayimi20241301)
async def get_depo_sayimi_2024_13_01_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2024_13_01_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi20241301)
async def create_depo_sayimi_2024_13_01_item(data: DepoSayimi20241301Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi20241301(**data.dict())
    return await create_depo_sayimi_2024_13_01(db, db_item)