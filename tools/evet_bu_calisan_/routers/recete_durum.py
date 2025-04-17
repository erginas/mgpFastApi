from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_durum import ReceteDurum, ReceteDurumCreate
from models.recete_durum import ReceteDurum as DBReceteDurum
from crud.recete_durum import get_all_recete_durum, get_recete_durum_by_id, create_recete_durum

router = APIRouter(prefix='/recete_durum', tags=['ReceteDurum'])

@router.get('/', response_model=list[ReceteDurum])
async def list_recete_durum(db: AsyncSession = Depends()):
    return await get_all_recete_durum(db)

@router.get('/{id}', response_model=ReceteDurum)
async def get_recete_durum_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_durum_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteDurum)
async def create_recete_durum_item(data: ReceteDurumCreate, db: AsyncSession = Depends()):
    db_item = DBReceteDurum(**data.dict())
    return await create_recete_durum(db, db_item)