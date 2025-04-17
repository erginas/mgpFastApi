from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.firma_degerlendirmesi import FirmaDegerlendirmesi, FirmaDegerlendirmesiCreate
from models.firma_degerlendirmesi import FirmaDegerlendirmesi as DBFirmaDegerlendirmesi
from crud.firma_degerlendirmesi import get_all_firma_degerlendirmesi, get_firma_degerlendirmesi_by_id, create_firma_degerlendirmesi

router = APIRouter(prefix='/firma_degerlendirmesi', tags=['FirmaDegerlendirmesi'])

@router.get('/', response_model=list[FirmaDegerlendirmesi])
async def list_firma_degerlendirmesi(db: AsyncSession = Depends()):
    return await get_all_firma_degerlendirmesi(db)

@router.get('/{id}', response_model=FirmaDegerlendirmesi)
async def get_firma_degerlendirmesi_item(id: int, db: AsyncSession = Depends()):
    result = await get_firma_degerlendirmesi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FirmaDegerlendirmesi)
async def create_firma_degerlendirmesi_item(data: FirmaDegerlendirmesiCreate, db: AsyncSession = Depends()):
    db_item = DBFirmaDegerlendirmesi(**data.dict())
    return await create_firma_degerlendirmesi(db, db_item)