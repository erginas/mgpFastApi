from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sistem_rolu import SistemRolu, SistemRoluCreate
from models.sistem_rolu import SistemRolu as DBSistemRolu
from crud.sistem_rolu import get_all_sistem_rolu, get_sistem_rolu_by_id, create_sistem_rolu

router = APIRouter(prefix='/sistem_rolu', tags=['SistemRolu'])

@router.get('/', response_model=list[SistemRolu])
async def list_sistem_rolu(db: AsyncSession = Depends()):
    return await get_all_sistem_rolu(db)

@router.get('/{id}', response_model=SistemRolu)
async def get_sistem_rolu_item(id: int, db: AsyncSession = Depends()):
    result = await get_sistem_rolu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SistemRolu)
async def create_sistem_rolu_item(data: SistemRoluCreate, db: AsyncSession = Depends()):
    db_item = DBSistemRolu(**data.dict())
    return await create_sistem_rolu(db, db_item)