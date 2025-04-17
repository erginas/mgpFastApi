from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sut_fiyat_detay import SutFiyatDetay, SutFiyatDetayCreate
from models.sut_fiyat_detay import SutFiyatDetay as DBSutFiyatDetay
from crud.sut_fiyat_detay import get_all_sut_fiyat_detay, get_sut_fiyat_detay_by_id, create_sut_fiyat_detay

router = APIRouter(prefix='/sut_fiyat_detay', tags=['SutFiyatDetay'])

@router.get('/', response_model=list[SutFiyatDetay])
async def list_sut_fiyat_detay(db: AsyncSession = Depends()):
    return await get_all_sut_fiyat_detay(db)

@router.get('/{id}', response_model=SutFiyatDetay)
async def get_sut_fiyat_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_sut_fiyat_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SutFiyatDetay)
async def create_sut_fiyat_detay_item(data: SutFiyatDetayCreate, db: AsyncSession = Depends()):
    db_item = DBSutFiyatDetay(**data.dict())
    return await create_sut_fiyat_detay(db, db_item)