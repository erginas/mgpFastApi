from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sut_fiyat import SutFiyat, SutFiyatCreate
from models.sut_fiyat import SutFiyat as DBSutFiyat
from crud.sut_fiyat import get_all_sut_fiyat, get_sut_fiyat_by_id, create_sut_fiyat

router = APIRouter(prefix='/sut_fiyat', tags=['SutFiyat'])

@router.get('/', response_model=list[SutFiyat])
async def list_sut_fiyat(db: AsyncSession = Depends()):
    return await get_all_sut_fiyat(db)

@router.get('/{id}', response_model=SutFiyat)
async def get_sut_fiyat_item(id: int, db: AsyncSession = Depends()):
    result = await get_sut_fiyat_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SutFiyat)
async def create_sut_fiyat_item(data: SutFiyatCreate, db: AsyncSession = Depends()):
    db_item = DBSutFiyat(**data.dict())
    return await create_sut_fiyat(db, db_item)