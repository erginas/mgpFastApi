from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.para_birimi_detay import ParaBirimiDetay, ParaBirimiDetayCreate
from models.para_birimi_detay import ParaBirimiDetay as DBParaBirimiDetay
from crud.para_birimi_detay import get_all_para_birimi_detay, get_para_birimi_detay_by_id, create_para_birimi_detay

router = APIRouter(prefix='/para_birimi_detay', tags=['ParaBirimiDetay'])

@router.get('/', response_model=list[ParaBirimiDetay])
async def list_para_birimi_detay(db: AsyncSession = Depends()):
    return await get_all_para_birimi_detay(db)

@router.get('/{id}', response_model=ParaBirimiDetay)
async def get_para_birimi_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_para_birimi_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ParaBirimiDetay)
async def create_para_birimi_detay_item(data: ParaBirimiDetayCreate, db: AsyncSession = Depends()):
    db_item = DBParaBirimiDetay(**data.dict())
    return await create_para_birimi_detay(db, db_item)