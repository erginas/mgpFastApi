from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_talep_detay import UretimTalepDetay, UretimTalepDetayCreate
from models.uretim_talep_detay import UretimTalepDetay as DBUretimTalepDetay
from crud.uretim_talep_detay import get_all_uretim_talep_detay, get_uretim_talep_detay_by_id, create_uretim_talep_detay

router = APIRouter(prefix='/uretim_talep_detay', tags=['UretimTalepDetay'])

@router.get('/', response_model=list[UretimTalepDetay])
async def list_uretim_talep_detay(db: AsyncSession = Depends()):
    return await get_all_uretim_talep_detay(db)

@router.get('/{id}', response_model=UretimTalepDetay)
async def get_uretim_talep_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_talep_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimTalepDetay)
async def create_uretim_talep_detay_item(data: UretimTalepDetayCreate, db: AsyncSession = Depends()):
    db_item = DBUretimTalepDetay(**data.dict())
    return await create_uretim_talep_detay(db, db_item)