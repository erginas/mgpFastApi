from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sk_plani import SkPlani, SkPlaniCreate
from models.sk_plani import SkPlani as DBSkPlani
from crud.sk_plani import get_all_sk_plani, get_sk_plani_by_id, create_sk_plani

router = APIRouter(prefix='/sk_plani', tags=['SkPlani'])

@router.get('/', response_model=list[SkPlani])
async def list_sk_plani(db: AsyncSession = Depends()):
    return await get_all_sk_plani(db)

@router.get('/{id}', response_model=SkPlani)
async def get_sk_plani_item(id: int, db: AsyncSession = Depends()):
    result = await get_sk_plani_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SkPlani)
async def create_sk_plani_item(data: SkPlaniCreate, db: AsyncSession = Depends()):
    db_item = DBSkPlani(**data.dict())
    return await create_sk_plani(db, db_item)