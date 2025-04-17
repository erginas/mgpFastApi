from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.veri_duzeltme_detayi import VeriDuzeltmeDetayi, VeriDuzeltmeDetayiCreate
from models.veri_duzeltme_detayi import VeriDuzeltmeDetayi as DBVeriDuzeltmeDetayi
from crud.veri_duzeltme_detayi import get_all_veri_duzeltme_detayi, get_veri_duzeltme_detayi_by_id, create_veri_duzeltme_detayi

router = APIRouter(prefix='/veri_duzeltme_detayi', tags=['VeriDuzeltmeDetayi'])

@router.get('/', response_model=list[VeriDuzeltmeDetayi])
async def list_veri_duzeltme_detayi(db: AsyncSession = Depends()):
    return await get_all_veri_duzeltme_detayi(db)

@router.get('/{id}', response_model=VeriDuzeltmeDetayi)
async def get_veri_duzeltme_detayi_item(id: int, db: AsyncSession = Depends()):
    result = await get_veri_duzeltme_detayi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=VeriDuzeltmeDetayi)
async def create_veri_duzeltme_detayi_item(data: VeriDuzeltmeDetayiCreate, db: AsyncSession = Depends()):
    db_item = DBVeriDuzeltmeDetayi(**data.dict())
    return await create_veri_duzeltme_detayi(db, db_item)