from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2008_01_ha import DepoSayimi200801Ha, DepoSayimi200801HaCreate
from models.depo_sayimi_2008_01_ha import DepoSayimi200801Ha as DBDepoSayimi200801Ha
from crud.depo_sayimi_2008_01_ha import get_all_depo_sayimi_2008_01_ha, get_depo_sayimi_2008_01_ha_by_id, create_depo_sayimi_2008_01_ha

router = APIRouter(prefix='/depo_sayimi_2008_01_ha', tags=['DepoSayimi200801Ha'])

@router.get('/', response_model=list[DepoSayimi200801Ha])
async def list_depo_sayimi_2008_01_ha(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2008_01_ha(db)

@router.get('/{id}', response_model=DepoSayimi200801Ha)
async def get_depo_sayimi_2008_01_ha_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2008_01_ha_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi200801Ha)
async def create_depo_sayimi_2008_01_ha_item(data: DepoSayimi200801HaCreate, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi200801Ha(**data.dict())
    return await create_depo_sayimi_2008_01_ha(db, db_item)