from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.hammadde_sertifikasi import HammaddeSertifikasi, HammaddeSertifikasiCreate
from models.hammadde_sertifikasi import HammaddeSertifikasi as DBHammaddeSertifikasi
from crud.hammadde_sertifikasi import get_all_hammadde_sertifikasi, get_hammadde_sertifikasi_by_id, create_hammadde_sertifikasi

router = APIRouter(prefix='/hammadde_sertifikasi', tags=['HammaddeSertifikasi'])

@router.get('/', response_model=list[HammaddeSertifikasi])
async def list_hammadde_sertifikasi(db: AsyncSession = Depends()):
    return await get_all_hammadde_sertifikasi(db)

@router.get('/{id}', response_model=HammaddeSertifikasi)
async def get_hammadde_sertifikasi_item(id: int, db: AsyncSession = Depends()):
    result = await get_hammadde_sertifikasi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=HammaddeSertifikasi)
async def create_hammadde_sertifikasi_item(data: HammaddeSertifikasiCreate, db: AsyncSession = Depends()):
    db_item = DBHammaddeSertifikasi(**data.dict())
    return await create_hammadde_sertifikasi(db, db_item)