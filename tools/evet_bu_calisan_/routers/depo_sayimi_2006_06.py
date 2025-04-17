from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2006_06 import DepoSayimi200606, DepoSayimi200606Create
from models.depo_sayimi_2006_06 import DepoSayimi200606 as DBDepoSayimi200606
from crud.depo_sayimi_2006_06 import get_all_depo_sayimi_2006_06, get_depo_sayimi_2006_06_by_id, create_depo_sayimi_2006_06

router = APIRouter(prefix='/depo_sayimi_2006_06', tags=['DepoSayimi200606'])

@router.get('/', response_model=list[DepoSayimi200606])
async def list_depo_sayimi_2006_06(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2006_06(db)

@router.get('/{id}', response_model=DepoSayimi200606)
async def get_depo_sayimi_2006_06_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2006_06_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi200606)
async def create_depo_sayimi_2006_06_item(data: DepoSayimi200606Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi200606(**data.dict())
    return await create_depo_sayimi_2006_06(db, db_item)