from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_hareket_sebebi import DepoHareketSebebi, DepoHareketSebebiCreate
from models.depo_hareket_sebebi import DepoHareketSebebi as DBDepoHareketSebebi
from crud.depo_hareket_sebebi import get_all_depo_hareket_sebebi, get_depo_hareket_sebebi_by_id, create_depo_hareket_sebebi

router = APIRouter(prefix='/depo_hareket_sebebi', tags=['DepoHareketSebebi'])

@router.get('/', response_model=list[DepoHareketSebebi])
async def list_depo_hareket_sebebi(db: AsyncSession = Depends()):
    return await get_all_depo_hareket_sebebi(db)

@router.get('/{id}', response_model=DepoHareketSebebi)
async def get_depo_hareket_sebebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_hareket_sebebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoHareketSebebi)
async def create_depo_hareket_sebebi_item(data: DepoHareketSebebiCreate, db: AsyncSession = Depends()):
    db_item = DBDepoHareketSebebi(**data.dict())
    return await create_depo_hareket_sebebi(db, db_item)