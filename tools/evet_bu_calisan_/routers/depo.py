from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo import Depo, DepoCreate
from models.depo import Depo as DBDepo
from crud.depo import get_all_depo, get_depo_by_id, create_depo

router = APIRouter(prefix='/depo', tags=['Depo'])

@router.get('/', response_model=list[Depo])
async def list_depo(db: AsyncSession = Depends()):
    return await get_all_depo(db)

@router.get('/{id}', response_model=Depo)
async def get_depo_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Depo)
async def create_depo_item(data: DepoCreate, db: AsyncSession = Depends()):
    db_item = DBDepo(**data.dict())
    return await create_depo(db, db_item)