from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_uretim_asamasi import ReceteUretimAsamasi, ReceteUretimAsamasiCreate
from models.recete_uretim_asamasi import ReceteUretimAsamasi as DBReceteUretimAsamasi
from crud.recete_uretim_asamasi import get_all_recete_uretim_asamasi, get_recete_uretim_asamasi_by_id, create_recete_uretim_asamasi

router = APIRouter(prefix='/recete_uretim_asamasi', tags=['ReceteUretimAsamasi'])

@router.get('/', response_model=list[ReceteUretimAsamasi])
async def list_recete_uretim_asamasi(db: AsyncSession = Depends()):
    return await get_all_recete_uretim_asamasi(db)

@router.get('/{id}', response_model=ReceteUretimAsamasi)
async def get_recete_uretim_asamasi_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_uretim_asamasi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteUretimAsamasi)
async def create_recete_uretim_asamasi_item(data: ReceteUretimAsamasiCreate, db: AsyncSession = Depends()):
    db_item = DBReceteUretimAsamasi(**data.dict())
    return await create_recete_uretim_asamasi(db, db_item)