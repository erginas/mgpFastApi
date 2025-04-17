from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uretim_emri_tipi_yetkilisi import UretimEmriTipiYetkilisi, UretimEmriTipiYetkilisiCreate
from models.uretim_emri_tipi_yetkilisi import UretimEmriTipiYetkilisi as DBUretimEmriTipiYetkilisi
from crud.uretim_emri_tipi_yetkilisi import get_all_uretim_emri_tipi_yetkilisi, get_uretim_emri_tipi_yetkilisi_by_id, create_uretim_emri_tipi_yetkilisi

router = APIRouter(prefix='/uretim_emri_tipi_yetkilisi', tags=['UretimEmriTipiYetkilisi'])

@router.get('/', response_model=list[UretimEmriTipiYetkilisi])
async def list_uretim_emri_tipi_yetkilisi(db: AsyncSession = Depends()):
    return await get_all_uretim_emri_tipi_yetkilisi(db)

@router.get('/{id}', response_model=UretimEmriTipiYetkilisi)
async def get_uretim_emri_tipi_yetkilisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_uretim_emri_tipi_yetkilisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UretimEmriTipiYetkilisi)
async def create_uretim_emri_tipi_yetkilisi_item(data: UretimEmriTipiYetkilisiCreate, db: AsyncSession = Depends()):
    db_item = DBUretimEmriTipiYetkilisi(**data.dict())
    return await create_uretim_emri_tipi_yetkilisi(db, db_item)