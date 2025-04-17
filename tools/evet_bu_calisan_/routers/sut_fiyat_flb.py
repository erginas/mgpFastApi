from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sut_fiyat_flb import SutFiyatFlb, SutFiyatFlbCreate
from models.sut_fiyat_flb import SutFiyatFlb as DBSutFiyatFlb
from crud.sut_fiyat_flb import get_all_sut_fiyat_flb, get_sut_fiyat_flb_by_id, create_sut_fiyat_flb

router = APIRouter(prefix='/sut_fiyat_flb', tags=['SutFiyatFlb'])

@router.get('/', response_model=list[SutFiyatFlb])
async def list_sut_fiyat_flb(db: AsyncSession = Depends()):
    return await get_all_sut_fiyat_flb(db)

@router.get('/{id}', response_model=SutFiyatFlb)
async def get_sut_fiyat_flb_item(id: int, db: AsyncSession = Depends()):
    result = await get_sut_fiyat_flb_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SutFiyatFlb)
async def create_sut_fiyat_flb_item(data: SutFiyatFlbCreate, db: AsyncSession = Depends()):
    db_item = DBSutFiyatFlb(**data.dict())
    return await create_sut_fiyat_flb(db, db_item)