from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_asamasi import UretimAsamasi, UretimAsamasiCreate
from models.uretim_asamasi import UretimAsamasi as DBUretimAsamasi
from crud.uretim_asamasi import get_all_uretim_asamasi, get_uretim_asamasi_by_id, create_uretim_asamasi

router = APIRouter(prefix='/uretim_asamasi', tags=['UretimAsamasi'])

@router.get('/', response_model=list[UretimAsamasi])
async def list_uretim_asamasi(db: AsyncSession = Depends()):
    return await get_all_uretim_asamasi(db)

@router.get('/{id}', response_model=UretimAsamasi)
async def get_uretim_asamasi_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_asamasi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimAsamasi)
async def create_uretim_asamasi_item(data: UretimAsamasiCreate, db: AsyncSession = Depends()):
    db_item = DBUretimAsamasi(**data.dict())
    return await create_uretim_asamasi(db, db_item)