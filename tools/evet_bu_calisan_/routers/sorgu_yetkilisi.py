from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sorgu_yetkilisi import SorguYetkilisi, SorguYetkilisiCreate
from models.sorgu_yetkilisi import SorguYetkilisi as DBSorguYetkilisi
from crud.sorgu_yetkilisi import get_all_sorgu_yetkilisi, get_sorgu_yetkilisi_by_id, create_sorgu_yetkilisi

router = APIRouter(prefix='/sorgu_yetkilisi', tags=['SorguYetkilisi'])

@router.get('/', response_model=list[SorguYetkilisi])
async def list_sorgu_yetkilisi(db: AsyncSession = Depends()):
    return await get_all_sorgu_yetkilisi(db)

@router.get('/{id}', response_model=SorguYetkilisi)
async def get_sorgu_yetkilisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_sorgu_yetkilisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SorguYetkilisi)
async def create_sorgu_yetkilisi_item(data: SorguYetkilisiCreate, db: AsyncSession = Depends()):
    db_item = DBSorguYetkilisi(**data.dict())
    return await create_sorgu_yetkilisi(db, db_item)