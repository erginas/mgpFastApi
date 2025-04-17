from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.firma_sertifikasi import FirmaSertifikasi, FirmaSertifikasiCreate
from models.firma_sertifikasi import FirmaSertifikasi as DBFirmaSertifikasi
from crud.firma_sertifikasi import get_all_firma_sertifikasi, get_firma_sertifikasi_by_id, create_firma_sertifikasi

router = APIRouter(prefix='/firma_sertifikasi', tags=['FirmaSertifikasi'])

@router.get('/', response_model=list[FirmaSertifikasi])
async def list_firma_sertifikasi(db: AsyncSession = Depends()):
    return await get_all_firma_sertifikasi(db)

@router.get('/{id}', response_model=FirmaSertifikasi)
async def get_firma_sertifikasi_item(id: int, db: AsyncSession = Depends()):
    result = await get_firma_sertifikasi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FirmaSertifikasi)
async def create_firma_sertifikasi_item(data: FirmaSertifikasiCreate, db: AsyncSession = Depends()):
    db_item = DBFirmaSertifikasi(**data.dict())
    return await create_firma_sertifikasi(db, db_item)