from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.atama import Atama, AtamaCreate
from models.atama import Atama as DBAtama
from crud.atama import get_all_atama, get_atama_by_id, create_atama

router = APIRouter(prefix='/atama', tags=['Atama'])

@router.get('/', response_model=list[Atama])
async def list_atama(db: AsyncSession = Depends()):
    return await get_all_atama(db)

@router.get('/{id}', response_model=Atama)
async def get_atama_item(id: int, db: AsyncSession = Depends()):
    result = await get_atama_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Atama)
async def create_atama_item(data: AtamaCreate, db: AsyncSession = Depends()):
    db_item = DBAtama(**data.dict())
    return await create_atama(db, db_item)