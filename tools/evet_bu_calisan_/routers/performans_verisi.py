from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.performans_verisi import PerformansVerisi, PerformansVerisiCreate
from models.performans_verisi import PerformansVerisi as DBPerformansVerisi
from crud.performans_verisi import get_all_performans_verisi, get_performans_verisi_by_id, create_performans_verisi

router = APIRouter(prefix='/performans_verisi', tags=['PerformansVerisi'])

@router.get('/', response_model=list[PerformansVerisi])
async def list_performans_verisi(db: AsyncSession = Depends()):
    return await get_all_performans_verisi(db)

@router.get('/{id}', response_model=PerformansVerisi)
async def get_performans_verisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_performans_verisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=PerformansVerisi)
async def create_performans_verisi_item(data: PerformansVerisiCreate, db: AsyncSession = Depends()):
    db_item = DBPerformansVerisi(**data.dict())
    return await create_performans_verisi(db, db_item)