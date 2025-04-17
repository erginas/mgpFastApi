from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sut_fiyat_master import SutFiyatMaster, SutFiyatMasterCreate
from models.sut_fiyat_master import SutFiyatMaster as DBSutFiyatMaster
from crud.sut_fiyat_master import get_all_sut_fiyat_master, get_sut_fiyat_master_by_id, create_sut_fiyat_master

router = APIRouter(prefix='/sut_fiyat_master', tags=['SutFiyatMaster'])

@router.get('/', response_model=list[SutFiyatMaster])
async def list_sut_fiyat_master(db: AsyncSession = Depends()):
    return await get_all_sut_fiyat_master(db)

@router.get('/{id}', response_model=SutFiyatMaster)
async def get_sut_fiyat_master_item(id: int, db: AsyncSession = Depends()):
    result = await get_sut_fiyat_master_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SutFiyatMaster)
async def create_sut_fiyat_master_item(data: SutFiyatMasterCreate, db: AsyncSession = Depends()):
    db_item = DBSutFiyatMaster(**data.dict())
    return await create_sut_fiyat_master(db, db_item)