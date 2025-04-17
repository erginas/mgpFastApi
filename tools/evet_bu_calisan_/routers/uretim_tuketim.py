from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_tuketim import UretimTuketim, UretimTuketimCreate
from models.uretim_tuketim import UretimTuketim as DBUretimTuketim
from crud.uretim_tuketim import get_all_uretim_tuketim, get_uretim_tuketim_by_id, create_uretim_tuketim

router = APIRouter(prefix='/uretim_tuketim', tags=['UretimTuketim'])

@router.get('/', response_model=list[UretimTuketim])
async def list_uretim_tuketim(db: AsyncSession = Depends()):
    return await get_all_uretim_tuketim(db)

@router.get('/{id}', response_model=UretimTuketim)
async def get_uretim_tuketim_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_tuketim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimTuketim)
async def create_uretim_tuketim_item(data: UretimTuketimCreate, db: AsyncSession = Depends()):
    db_item = DBUretimTuketim(**data.dict())
    return await create_uretim_tuketim(db, db_item)