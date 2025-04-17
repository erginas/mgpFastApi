from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.toplanti import Toplanti, ToplantiCreate
from models.toplanti import Toplanti as DBToplanti
from crud.toplanti import get_all_toplanti, get_toplanti_by_id, create_toplanti

router = APIRouter(prefix='/toplanti', tags=['Toplanti'])

@router.get('/', response_model=list[Toplanti])
async def list_toplanti(db: AsyncSession = Depends()):
    return await get_all_toplanti(db)

@router.get('/{id}', response_model=Toplanti)
async def get_toplanti_item(id: int, db: AsyncSession = Depends()):
    result = await get_toplanti_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Toplanti)
async def create_toplanti_item(data: ToplantiCreate, db: AsyncSession = Depends()):
    db_item = DBToplanti(**data.dict())
    return await create_toplanti(db, db_item)