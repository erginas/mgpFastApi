from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.fiyat_tarifesi import FiyatTarifesi, FiyatTarifesiCreate
from models.fiyat_tarifesi import FiyatTarifesi as DBFiyatTarifesi
from crud.fiyat_tarifesi import get_all_fiyat_tarifesi, get_fiyat_tarifesi_by_id, create_fiyat_tarifesi

router = APIRouter(prefix='/fiyat_tarifesi', tags=['FiyatTarifesi'])

@router.get('/', response_model=list[FiyatTarifesi])
async def list_fiyat_tarifesi(db: AsyncSession = Depends()):
    return await get_all_fiyat_tarifesi(db)

@router.get('/{id}', response_model=FiyatTarifesi)
async def get_fiyat_tarifesi_item(id: int, db: AsyncSession = Depends()):
    result = await get_fiyat_tarifesi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FiyatTarifesi)
async def create_fiyat_tarifesi_item(data: FiyatTarifesiCreate, db: AsyncSession = Depends()):
    db_item = DBFiyatTarifesi(**data.dict())
    return await create_fiyat_tarifesi(db, db_item)