from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.hammadde_sertifika_referansi import HammaddeSertifikaReferansi, HammaddeSertifikaReferansiCreate
from models.hammadde_sertifika_referansi import HammaddeSertifikaReferansi as DBHammaddeSertifikaReferansi
from crud.hammadde_sertifika_referansi import get_all_hammadde_sertifika_referansi, get_hammadde_sertifika_referansi_by_id, create_hammadde_sertifika_referansi

router = APIRouter(prefix='/hammadde_sertifika_referansi', tags=['HammaddeSertifikaReferansi'])

@router.get('/', response_model=list[HammaddeSertifikaReferansi])
async def list_hammadde_sertifika_referansi(db: AsyncSession = Depends()):
    return await get_all_hammadde_sertifika_referansi(db)

@router.get('/{id}', response_model=HammaddeSertifikaReferansi)
async def get_hammadde_sertifika_referansi_item(id: int, db: AsyncSession = Depends()):
    result = await get_hammadde_sertifika_referansi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=HammaddeSertifikaReferansi)
async def create_hammadde_sertifika_referansi_item(data: HammaddeSertifikaReferansiCreate, db: AsyncSession = Depends()):
    db_item = DBHammaddeSertifikaReferansi(**data.dict())
    return await create_hammadde_sertifika_referansi(db, db_item)