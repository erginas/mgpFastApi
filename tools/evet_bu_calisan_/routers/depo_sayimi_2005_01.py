from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2005_01 import DepoSayimi200501, DepoSayimi200501Create
from models.depo_sayimi_2005_01 import DepoSayimi200501 as DBDepoSayimi200501
from crud.depo_sayimi_2005_01 import get_all_depo_sayimi_2005_01, get_depo_sayimi_2005_01_by_id, create_depo_sayimi_2005_01

router = APIRouter(prefix='/depo_sayimi_2005_01', tags=['DepoSayimi200501'])

@router.get('/', response_model=list[DepoSayimi200501])
async def list_depo_sayimi_2005_01(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2005_01(db)

@router.get('/{id}', response_model=DepoSayimi200501)
async def get_depo_sayimi_2005_01_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2005_01_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi200501)
async def create_depo_sayimi_2005_01_item(data: DepoSayimi200501Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi200501(**data.dict())
    return await create_depo_sayimi_2005_01(db, db_item)