from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kadro import Kadro, KadroCreate
from models.kadro import Kadro as DBKadro
from crud.kadro import get_all_kadro, get_kadro_by_id, create_kadro

router = APIRouter(prefix='/kadro', tags=['Kadro'])

@router.get('/', response_model=list[Kadro])
async def list_kadro(db: AsyncSession = Depends()):
    return await get_all_kadro(db)

@router.get('/{id}', response_model=Kadro)
async def get_kadro_item(id: int, db: AsyncSession = Depends()):
    result = await get_kadro_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Kadro)
async def create_kadro_item(data: KadroCreate, db: AsyncSession = Depends()):
    db_item = DBKadro(**data.dict())
    return await create_kadro(db, db_item)