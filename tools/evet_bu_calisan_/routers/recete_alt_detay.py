from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_alt_detay import ReceteAltDetay, ReceteAltDetayCreate
from models.recete_alt_detay import ReceteAltDetay as DBReceteAltDetay
from crud.recete_alt_detay import get_all_recete_alt_detay, get_recete_alt_detay_by_id, create_recete_alt_detay

router = APIRouter(prefix='/recete_alt_detay', tags=['ReceteAltDetay'])

@router.get('/', response_model=list[ReceteAltDetay])
async def list_recete_alt_detay(db: AsyncSession = Depends()):
    return await get_all_recete_alt_detay(db)

@router.get('/{id}', response_model=ReceteAltDetay)
async def get_recete_alt_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_alt_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteAltDetay)
async def create_recete_alt_detay_item(data: ReceteAltDetayCreate, db: AsyncSession = Depends()):
    db_item = DBReceteAltDetay(**data.dict())
    return await create_recete_alt_detay(db, db_item)