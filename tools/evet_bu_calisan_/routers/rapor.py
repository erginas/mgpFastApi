from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.rapor import Rapor, RaporCreate
from models.rapor import Rapor as DBRapor
from crud.rapor import get_all_rapor, get_rapor_by_id, create_rapor

router = APIRouter(prefix='/rapor', tags=['Rapor'])

@router.get('/', response_model=list[Rapor])
async def list_rapor(db: AsyncSession = Depends()):
    return await get_all_rapor(db)

@router.get('/{id}', response_model=Rapor)
async def get_rapor_item(id: int, db: AsyncSession = Depends()):
    result = await get_rapor_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Rapor)
async def create_rapor_item(data: RaporCreate, db: AsyncSession = Depends()):
    db_item = DBRapor(**data.dict())
    return await create_rapor(db, db_item)