from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2019_12_12 import DepoSayimi20191212, DepoSayimi20191212Create
from models.depo_sayimi_2019_12_12 import DepoSayimi20191212 as DBDepoSayimi20191212
from crud.depo_sayimi_2019_12_12 import get_all_depo_sayimi_2019_12_12, get_depo_sayimi_2019_12_12_by_id, create_depo_sayimi_2019_12_12

router = APIRouter(prefix='/depo_sayimi_2019_12_12', tags=['DepoSayimi20191212'])

@router.get('/', response_model=list[DepoSayimi20191212])
async def list_depo_sayimi_2019_12_12(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2019_12_12(db)

@router.get('/{id}', response_model=DepoSayimi20191212)
async def get_depo_sayimi_2019_12_12_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2019_12_12_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi20191212)
async def create_depo_sayimi_2019_12_12_item(data: DepoSayimi20191212Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi20191212(**data.dict())
    return await create_depo_sayimi_2019_12_12(db, db_item)