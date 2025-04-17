from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.performans import Performans, PerformansCreate
from models.performans import Performans as DBPerformans
from crud.performans import get_all_performans, get_performans_by_id, create_performans

router = APIRouter(prefix='/performans', tags=['Performans'])

@router.get('/', response_model=list[Performans])
async def list_performans(db: AsyncSession = Depends()):
    return await get_all_performans(db)

@router.get('/{id}', response_model=Performans)
async def get_performans_item(id: int, db: AsyncSession = Depends()):
    result = await get_performans_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Performans)
async def create_performans_item(data: PerformansCreate, db: AsyncSession = Depends()):
    db_item = DBPerformans(**data.dict())
    return await create_performans(db, db_item)