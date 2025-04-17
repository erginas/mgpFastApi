from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2006_01 import DepoSayimi200601, DepoSayimi200601Create
from models.depo_sayimi_2006_01 import DepoSayimi200601 as DBDepoSayimi200601
from crud.depo_sayimi_2006_01 import get_all_depo_sayimi_2006_01, get_depo_sayimi_2006_01_by_id, create_depo_sayimi_2006_01

router = APIRouter(prefix='/depo_sayimi_2006_01', tags=['DepoSayimi200601'])

@router.get('/', response_model=list[DepoSayimi200601])
async def list_depo_sayimi_2006_01(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2006_01(db)

@router.get('/{id}', response_model=DepoSayimi200601)
async def get_depo_sayimi_2006_01_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2006_01_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi200601)
async def create_depo_sayimi_2006_01_item(data: DepoSayimi200601Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi200601(**data.dict())
    return await create_depo_sayimi_2006_01(db, db_item)