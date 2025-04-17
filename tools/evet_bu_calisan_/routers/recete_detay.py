from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_detay import ReceteDetay, ReceteDetayCreate
from models.recete_detay import ReceteDetay as DBReceteDetay
from crud.recete_detay import get_all_recete_detay, get_recete_detay_by_id, create_recete_detay

router = APIRouter(prefix='/recete_detay', tags=['ReceteDetay'])

@router.get('/', response_model=list[ReceteDetay])
async def list_recete_detay(db: AsyncSession = Depends()):
    return await get_all_recete_detay(db)

@router.get('/{id}', response_model=ReceteDetay)
async def get_recete_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteDetay)
async def create_recete_detay_item(data: ReceteDetayCreate, db: AsyncSession = Depends()):
    db_item = DBReceteDetay(**data.dict())
    return await create_recete_detay(db, db_item)