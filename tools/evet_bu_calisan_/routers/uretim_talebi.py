from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_talebi import UretimTalebi, UretimTalebiCreate
from models.uretim_talebi import UretimTalebi as DBUretimTalebi
from crud.uretim_talebi import get_all_uretim_talebi, get_uretim_talebi_by_id, create_uretim_talebi

router = APIRouter(prefix='/uretim_talebi', tags=['UretimTalebi'])

@router.get('/', response_model=list[UretimTalebi])
async def list_uretim_talebi(db: AsyncSession = Depends()):
    return await get_all_uretim_talebi(db)

@router.get('/{id}', response_model=UretimTalebi)
async def get_uretim_talebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_talebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimTalebi)
async def create_uretim_talebi_item(data: UretimTalebiCreate, db: AsyncSession = Depends()):
    db_item = DBUretimTalebi(**data.dict())
    return await create_uretim_talebi(db, db_item)