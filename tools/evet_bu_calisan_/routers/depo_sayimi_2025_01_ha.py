from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2025_01_ha import DepoSayimi202501Ha, DepoSayimi202501HaCreate
from models.depo_sayimi_2025_01_ha import DepoSayimi202501Ha as DBDepoSayimi202501Ha
from crud.depo_sayimi_2025_01_ha import get_all_depo_sayimi_2025_01_ha, get_depo_sayimi_2025_01_ha_by_id, create_depo_sayimi_2025_01_ha

router = APIRouter(prefix='/depo_sayimi_2025_01_ha', tags=['DepoSayimi202501Ha'])

@router.get('/', response_model=list[DepoSayimi202501Ha])
async def list_depo_sayimi_2025_01_ha(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2025_01_ha(db)

@router.get('/{id}', response_model=DepoSayimi202501Ha)
async def get_depo_sayimi_2025_01_ha_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2025_01_ha_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi202501Ha)
async def create_depo_sayimi_2025_01_ha_item(data: DepoSayimi202501HaCreate, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi202501Ha(**data.dict())
    return await create_depo_sayimi_2025_01_ha(db, db_item)