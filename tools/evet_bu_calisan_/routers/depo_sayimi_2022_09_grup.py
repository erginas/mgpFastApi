from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2022_09_grup import DepoSayimi202209Grup, DepoSayimi202209GrupCreate
from models.depo_sayimi_2022_09_grup import DepoSayimi202209Grup as DBDepoSayimi202209Grup
from crud.depo_sayimi_2022_09_grup import get_all_depo_sayimi_2022_09_grup, get_depo_sayimi_2022_09_grup_by_id, create_depo_sayimi_2022_09_grup

router = APIRouter(prefix='/depo_sayimi_2022_09_grup', tags=['DepoSayimi202209Grup'])

@router.get('/', response_model=list[DepoSayimi202209Grup])
async def list_depo_sayimi_2022_09_grup(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2022_09_grup(db)

@router.get('/{id}', response_model=DepoSayimi202209Grup)
async def get_depo_sayimi_2022_09_grup_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2022_09_grup_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi202209Grup)
async def create_depo_sayimi_2022_09_grup_item(data: DepoSayimi202209GrupCreate, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi202209Grup(**data.dict())
    return await create_depo_sayimi_2022_09_grup(db, db_item)