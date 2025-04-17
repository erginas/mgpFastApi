from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tcks import Tcks, TcksCreate
from models.tcks import Tcks as DBTcks
from crud.tcks import get_all_tcks, get_tcks_by_id, create_tcks

router = APIRouter(prefix='/tcks', tags=['Tcks'])

@router.get('/', response_model=list[Tcks])
async def list_tcks(db: AsyncSession = Depends()):
    return await get_all_tcks(db)

@router.get('/{id}', response_model=Tcks)
async def get_tcks_item(id: int, db: AsyncSession = Depends()):
    result = await get_tcks_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Tcks)
async def create_tcks_item(data: TcksCreate, db: AsyncSession = Depends()):
    db_item = DBTcks(**data.dict())
    return await create_tcks(db, db_item)