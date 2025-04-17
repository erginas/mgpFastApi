from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_uretim_tuketim import ReceteUretimTuketim, ReceteUretimTuketimCreate
from models.recete_uretim_tuketim import ReceteUretimTuketim as DBReceteUretimTuketim
from crud.recete_uretim_tuketim import get_all_recete_uretim_tuketim, get_recete_uretim_tuketim_by_id, create_recete_uretim_tuketim

router = APIRouter(prefix='/recete_uretim_tuketim', tags=['ReceteUretimTuketim'])

@router.get('/', response_model=list[ReceteUretimTuketim])
async def list_recete_uretim_tuketim(db: AsyncSession = Depends()):
    return await get_all_recete_uretim_tuketim(db)

@router.get('/{id}', response_model=ReceteUretimTuketim)
async def get_recete_uretim_tuketim_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_uretim_tuketim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteUretimTuketim)
async def create_recete_uretim_tuketim_item(data: ReceteUretimTuketimCreate, db: AsyncSession = Depends()):
    db_item = DBReceteUretimTuketim(**data.dict())
    return await create_recete_uretim_tuketim(db, db_item)