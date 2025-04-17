from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.aktar_sut_fiyat import AktarSutFiyat, AktarSutFiyatCreate
from models.aktar_sut_fiyat import AktarSutFiyat as DBAktarSutFiyat
from crud.aktar_sut_fiyat import get_all_aktar_sut_fiyat, get_aktar_sut_fiyat_by_id, create_aktar_sut_fiyat

router = APIRouter(prefix='/aktar_sut_fiyat', tags=['AktarSutFiyat'])

@router.get('/', response_model=list[AktarSutFiyat])
async def list_aktar_sut_fiyat(db: AsyncSession = Depends()):
    return await get_all_aktar_sut_fiyat(db)

@router.get('/{id}', response_model=AktarSutFiyat)
async def get_aktar_sut_fiyat_item(id: int, db: AsyncSession = Depends()):
    result = await get_aktar_sut_fiyat_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AktarSutFiyat)
async def create_aktar_sut_fiyat_item(data: AktarSutFiyatCreate, db: AsyncSession = Depends()):
    db_item = DBAktarSutFiyat(**data.dict())
    return await create_aktar_sut_fiyat(db, db_item)