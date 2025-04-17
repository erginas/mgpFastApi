from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_operasyonu import ReceteOperasyonu, ReceteOperasyonuCreate
from models.recete_operasyonu import ReceteOperasyonu as DBReceteOperasyonu
from crud.recete_operasyonu import get_all_recete_operasyonu, get_recete_operasyonu_by_id, create_recete_operasyonu

router = APIRouter(prefix='/recete_operasyonu', tags=['ReceteOperasyonu'])

@router.get('/', response_model=list[ReceteOperasyonu])
async def list_recete_operasyonu(db: AsyncSession = Depends()):
    return await get_all_recete_operasyonu(db)

@router.get('/{id}', response_model=ReceteOperasyonu)
async def get_recete_operasyonu_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_operasyonu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteOperasyonu)
async def create_recete_operasyonu_item(data: ReceteOperasyonuCreate, db: AsyncSession = Depends()):
    db_item = DBReceteOperasyonu(**data.dict())
    return await create_recete_operasyonu(db, db_item)