from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.veri_duzeltme_talebi import VeriDuzeltmeTalebi, VeriDuzeltmeTalebiCreate
from models.veri_duzeltme_talebi import VeriDuzeltmeTalebi as DBVeriDuzeltmeTalebi
from crud.veri_duzeltme_talebi import get_all_veri_duzeltme_talebi, get_veri_duzeltme_talebi_by_id, create_veri_duzeltme_talebi

router = APIRouter(prefix='/veri_duzeltme_talebi', tags=['VeriDuzeltmeTalebi'])

@router.get('/', response_model=list[VeriDuzeltmeTalebi])
async def list_veri_duzeltme_talebi(db: AsyncSession = Depends()):
    return await get_all_veri_duzeltme_talebi(db)

@router.get('/{id}', response_model=VeriDuzeltmeTalebi)
async def get_veri_duzeltme_talebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_veri_duzeltme_talebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=VeriDuzeltmeTalebi)
async def create_veri_duzeltme_talebi_item(data: VeriDuzeltmeTalebiCreate, db: AsyncSession = Depends()):
    db_item = DBVeriDuzeltmeTalebi(**data.dict())
    return await create_veri_duzeltme_talebi(db, db_item)