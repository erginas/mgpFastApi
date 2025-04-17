from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2024_13_1 import DepoSayimi2024131, DepoSayimi2024131Create
from models.depo_sayimi_2024_13_1 import DepoSayimi2024131 as DBDepoSayimi2024131
from crud.depo_sayimi_2024_13_1 import get_all_depo_sayimi_2024_13_1, get_depo_sayimi_2024_13_1_by_id, create_depo_sayimi_2024_13_1

router = APIRouter(prefix='/depo_sayimi_2024_13_1', tags=['DepoSayimi2024131'])

@router.get('/', response_model=list[DepoSayimi2024131])
async def list_depo_sayimi_2024_13_1(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2024_13_1(db)

@router.get('/{id}', response_model=DepoSayimi2024131)
async def get_depo_sayimi_2024_13_1_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2024_13_1_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi2024131)
async def create_depo_sayimi_2024_13_1_item(data: DepoSayimi2024131Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi2024131(**data.dict())
    return await create_depo_sayimi_2024_13_1(db, db_item)