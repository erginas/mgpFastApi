from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi import DepoSayimi, DepoSayimiCreate
from models.depo_sayimi import DepoSayimi as DBDepoSayimi
from crud.depo_sayimi import get_all_depo_sayimi, get_depo_sayimi_by_id, create_depo_sayimi

router = APIRouter(prefix='/depo_sayimi', tags=['DepoSayimi'])

@router.get('/', response_model=list[DepoSayimi])
async def list_depo_sayimi(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi(db)

@router.get('/{id}', response_model=DepoSayimi)
async def get_depo_sayimi_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi)
async def create_depo_sayimi_item(data: DepoSayimiCreate, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi(**data.dict())
    return await create_depo_sayimi(db, db_item)