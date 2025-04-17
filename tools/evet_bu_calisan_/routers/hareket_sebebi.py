from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.hareket_sebebi import HareketSebebi, HareketSebebiCreate
from models.hareket_sebebi import HareketSebebi as DBHareketSebebi
from crud.hareket_sebebi import get_all_hareket_sebebi, get_hareket_sebebi_by_id, create_hareket_sebebi

router = APIRouter(prefix='/hareket_sebebi', tags=['HareketSebebi'])

@router.get('/', response_model=list[HareketSebebi])
async def list_hareket_sebebi(db: AsyncSession = Depends()):
    return await get_all_hareket_sebebi(db)

@router.get('/{id}', response_model=HareketSebebi)
async def get_hareket_sebebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_hareket_sebebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=HareketSebebi)
async def create_hareket_sebebi_item(data: HareketSebebiCreate, db: AsyncSession = Depends()):
    db_item = DBHareketSebebi(**data.dict())
    return await create_hareket_sebebi(db, db_item)