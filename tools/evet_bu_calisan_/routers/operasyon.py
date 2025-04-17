from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.operasyon import Operasyon, OperasyonCreate
from models.operasyon import Operasyon as DBOperasyon
from crud.operasyon import get_all_operasyon, get_operasyon_by_id, create_operasyon

router = APIRouter(prefix='/operasyon', tags=['Operasyon'])

@router.get('/', response_model=list[Operasyon])
async def list_operasyon(db: AsyncSession = Depends()):
    return await get_all_operasyon(db)

@router.get('/{id}', response_model=Operasyon)
async def get_operasyon_item(id: int, db: AsyncSession = Depends()):
    result = await get_operasyon_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Operasyon)
async def create_operasyon_item(data: OperasyonCreate, db: AsyncSession = Depends()):
    db_item = DBOperasyon(**data.dict())
    return await create_operasyon(db, db_item)