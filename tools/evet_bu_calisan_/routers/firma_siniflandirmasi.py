from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.firma_siniflandirmasi import FirmaSiniflandirmasi, FirmaSiniflandirmasiCreate
from models.firma_siniflandirmasi import FirmaSiniflandirmasi as DBFirmaSiniflandirmasi
from crud.firma_siniflandirmasi import get_all_firma_siniflandirmasi, get_firma_siniflandirmasi_by_id, create_firma_siniflandirmasi

router = APIRouter(prefix='/firma_siniflandirmasi', tags=['FirmaSiniflandirmasi'])

@router.get('/', response_model=list[FirmaSiniflandirmasi])
async def list_firma_siniflandirmasi(db: AsyncSession = Depends()):
    return await get_all_firma_siniflandirmasi(db)

@router.get('/{id}', response_model=FirmaSiniflandirmasi)
async def get_firma_siniflandirmasi_item(id: int, db: AsyncSession = Depends()):
    result = await get_firma_siniflandirmasi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FirmaSiniflandirmasi)
async def create_firma_siniflandirmasi_item(data: FirmaSiniflandirmasiCreate, db: AsyncSession = Depends()):
    db_item = DBFirmaSiniflandirmasi(**data.dict())
    return await create_firma_siniflandirmasi(db, db_item)