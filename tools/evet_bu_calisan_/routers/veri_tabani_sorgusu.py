from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.veri_tabani_sorgusu import VeriTabaniSorgusu, VeriTabaniSorgusuCreate
from models.veri_tabani_sorgusu import VeriTabaniSorgusu as DBVeriTabaniSorgusu
from crud.veri_tabani_sorgusu import get_all_veri_tabani_sorgusu, get_veri_tabani_sorgusu_by_id, create_veri_tabani_sorgusu

router = APIRouter(prefix='/veri_tabani_sorgusu', tags=['VeriTabaniSorgusu'])

@router.get('/', response_model=list[VeriTabaniSorgusu])
async def list_veri_tabani_sorgusu(db: AsyncSession = Depends()):
    return await get_all_veri_tabani_sorgusu(db)

@router.get('/{id}', response_model=VeriTabaniSorgusu)
async def get_veri_tabani_sorgusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_veri_tabani_sorgusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=VeriTabaniSorgusu)
async def create_veri_tabani_sorgusu_item(data: VeriTabaniSorgusuCreate, db: AsyncSession = Depends()):
    db_item = DBVeriTabaniSorgusu(**data.dict())
    return await create_veri_tabani_sorgusu(db, db_item)