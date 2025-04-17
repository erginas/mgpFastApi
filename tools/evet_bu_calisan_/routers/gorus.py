from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.gorus import Gorus, GorusCreate
from models.gorus import Gorus as DBGorus
from crud.gorus import get_all_gorus, get_gorus_by_id, create_gorus

router = APIRouter(prefix='/gorus', tags=['Gorus'])

@router.get('/', response_model=list[Gorus])
async def list_gorus(db: AsyncSession = Depends()):
    return await get_all_gorus(db)

@router.get('/{id}', response_model=Gorus)
async def get_gorus_item(id: int, db: AsyncSession = Depends()):
    result = await get_gorus_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Gorus)
async def create_gorus_item(data: GorusCreate, db: AsyncSession = Depends()):
    db_item = DBGorus(**data.dict())
    return await create_gorus(db, db_item)