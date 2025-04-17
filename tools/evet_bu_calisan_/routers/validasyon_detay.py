from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.validasyon_detay import ValidasyonDetay, ValidasyonDetayCreate
from models.validasyon_detay import ValidasyonDetay as DBValidasyonDetay
from crud.validasyon_detay import get_all_validasyon_detay, get_validasyon_detay_by_id, create_validasyon_detay

router = APIRouter(prefix='/validasyon_detay', tags=['ValidasyonDetay'])

@router.get('/', response_model=list[ValidasyonDetay])
async def list_validasyon_detay(db: AsyncSession = Depends()):
    return await get_all_validasyon_detay(db)

@router.get('/{id}', response_model=ValidasyonDetay)
async def get_validasyon_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_validasyon_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ValidasyonDetay)
async def create_validasyon_detay_item(data: ValidasyonDetayCreate, db: AsyncSession = Depends()):
    db_item = DBValidasyonDetay(**data.dict())
    return await create_validasyon_detay(db, db_item)