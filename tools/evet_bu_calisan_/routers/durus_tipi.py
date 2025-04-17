from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.durus_tipi import DurusTipi, DurusTipiCreate
from models.durus_tipi import DurusTipi as DBDurusTipi
from crud.durus_tipi import get_all_durus_tipi, get_durus_tipi_by_id, create_durus_tipi

router = APIRouter(prefix='/durus_tipi', tags=['DurusTipi'])

@router.get('/', response_model=list[DurusTipi])
async def list_durus_tipi(db: AsyncSession = Depends()):
    return await get_all_durus_tipi(db)

@router.get('/{id}', response_model=DurusTipi)
async def get_durus_tipi_item(id: int, db: AsyncSession = Depends()):
    result = await get_durus_tipi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DurusTipi)
async def create_durus_tipi_item(data: DurusTipiCreate, db: AsyncSession = Depends()):
    db_item = DBDurusTipi(**data.dict())
    return await create_durus_tipi(db, db_item)