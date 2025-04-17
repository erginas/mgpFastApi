from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.yetkinlik import Yetkinlik, YetkinlikCreate
from models.yetkinlik import Yetkinlik as DBYetkinlik
from crud.yetkinlik import get_all_yetkinlik, get_yetkinlik_by_id, create_yetkinlik

router = APIRouter(prefix='/yetkinlik', tags=['Yetkinlik'])

@router.get('/', response_model=list[Yetkinlik])
async def list_yetkinlik(db: AsyncSession = Depends()):
    return await get_all_yetkinlik(db)

@router.get('/{id}', response_model=Yetkinlik)
async def get_yetkinlik_item(id: int, db: AsyncSession = Depends()):
    result = await get_yetkinlik_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Yetkinlik)
async def create_yetkinlik_item(data: YetkinlikCreate, db: AsyncSession = Depends()):
    db_item = DBYetkinlik(**data.dict())
    return await create_yetkinlik(db, db_item)