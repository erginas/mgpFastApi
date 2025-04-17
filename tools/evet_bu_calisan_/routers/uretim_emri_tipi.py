from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_emri_tipi import UretimEmriTipi, UretimEmriTipiCreate
from models.uretim_emri_tipi import UretimEmriTipi as DBUretimEmriTipi
from crud.uretim_emri_tipi import get_all_uretim_emri_tipi, get_uretim_emri_tipi_by_id, create_uretim_emri_tipi

router = APIRouter(prefix='/uretim_emri_tipi', tags=['UretimEmriTipi'])

@router.get('/', response_model=list[UretimEmriTipi])
async def list_uretim_emri_tipi(db: AsyncSession = Depends()):
    return await get_all_uretim_emri_tipi(db)

@router.get('/{id}', response_model=UretimEmriTipi)
async def get_uretim_emri_tipi_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_emri_tipi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimEmriTipi)
async def create_uretim_emri_tipi_item(data: UretimEmriTipiCreate, db: AsyncSession = Depends()):
    db_item = DBUretimEmriTipi(**data.dict())
    return await create_uretim_emri_tipi(db, db_item)