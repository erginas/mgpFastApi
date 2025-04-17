from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_yetkilisi import DepoYetkilisi, DepoYetkilisiCreate
from models.depo_yetkilisi import DepoYetkilisi as DBDepoYetkilisi
from crud.depo_yetkilisi import get_all_depo_yetkilisi, get_depo_yetkilisi_by_id, create_depo_yetkilisi

router = APIRouter(prefix='/depo_yetkilisi', tags=['DepoYetkilisi'])

@router.get('/', response_model=list[DepoYetkilisi])
async def list_depo_yetkilisi(db: AsyncSession = Depends()):
    return await get_all_depo_yetkilisi(db)

@router.get('/{id}', response_model=DepoYetkilisi)
async def get_depo_yetkilisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_yetkilisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoYetkilisi)
async def create_depo_yetkilisi_item(data: DepoYetkilisiCreate, db: AsyncSession = Depends()):
    db_item = DBDepoYetkilisi(**data.dict())
    return await create_depo_yetkilisi(db, db_item)