from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kalite_dosya import KaliteDosya, KaliteDosyaCreate
from models.kalite_dosya import KaliteDosya as DBKaliteDosya
from crud.kalite_dosya import get_all_kalite_dosya, get_kalite_dosya_by_id, create_kalite_dosya

router = APIRouter(prefix='/kalite_dosya', tags=['KaliteDosya'])

@router.get('/', response_model=list[KaliteDosya])
async def list_kalite_dosya(db: AsyncSession = Depends()):
    return await get_all_kalite_dosya(db)

@router.get('/{id}', response_model=KaliteDosya)
async def get_kalite_dosya_item(id: int, db: AsyncSession = Depends()):
    result = await get_kalite_dosya_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KaliteDosya)
async def create_kalite_dosya_item(data: KaliteDosyaCreate, db: AsyncSession = Depends()):
    db_item = DBKaliteDosya(**data.dict())
    return await create_kalite_dosya(db, db_item)