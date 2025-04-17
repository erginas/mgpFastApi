from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_takip_sistemi import UretimTakipSistemi, UretimTakipSistemiCreate
from models.uretim_takip_sistemi import UretimTakipSistemi as DBUretimTakipSistemi
from crud.uretim_takip_sistemi import get_all_uretim_takip_sistemi, get_uretim_takip_sistemi_by_id, create_uretim_takip_sistemi

router = APIRouter(prefix='/uretim_takip_sistemi', tags=['UretimTakipSistemi'])

@router.get('/', response_model=list[UretimTakipSistemi])
async def list_uretim_takip_sistemi(db: AsyncSession = Depends()):
    return await get_all_uretim_takip_sistemi(db)

@router.get('/{id}', response_model=UretimTakipSistemi)
async def get_uretim_takip_sistemi_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_takip_sistemi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimTakipSistemi)
async def create_uretim_takip_sistemi_item(data: UretimTakipSistemiCreate, db: AsyncSession = Depends()):
    db_item = DBUretimTakipSistemi(**data.dict())
    return await create_uretim_takip_sistemi(db, db_item)