from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.izin_talebi import IzinTalebi, IzinTalebiCreate
from models.izin_talebi import IzinTalebi as DBIzinTalebi
from crud.izin_talebi import get_all_izin_talebi, get_izin_talebi_by_id, create_izin_talebi

router = APIRouter(prefix='/izin_talebi', tags=['IzinTalebi'])

@router.get('/', response_model=list[IzinTalebi])
async def list_izin_talebi(db: AsyncSession = Depends()):
    return await get_all_izin_talebi(db)

@router.get('/{id}', response_model=IzinTalebi)
async def get_izin_talebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_izin_talebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IzinTalebi)
async def create_izin_talebi_item(data: IzinTalebiCreate, db: AsyncSession = Depends()):
    db_item = DBIzinTalebi(**data.dict())
    return await create_izin_talebi(db, db_item)