from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.satin_alma_talebi import SatinAlmaTalebi, SatinAlmaTalebiCreate
from models.satin_alma_talebi import SatinAlmaTalebi as DBSatinAlmaTalebi
from crud.satin_alma_talebi import get_all_satin_alma_talebi, get_satin_alma_talebi_by_id, create_satin_alma_talebi

router = APIRouter(prefix='/satin_alma_talebi', tags=['SatinAlmaTalebi'])

@router.get('/', response_model=list[SatinAlmaTalebi])
async def list_satin_alma_talebi(db: AsyncSession = Depends()):
    return await get_all_satin_alma_talebi(db)

@router.get('/{id}', response_model=SatinAlmaTalebi)
async def get_satin_alma_talebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_satin_alma_talebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SatinAlmaTalebi)
async def create_satin_alma_talebi_item(data: SatinAlmaTalebiCreate, db: AsyncSession = Depends()):
    db_item = DBSatinAlmaTalebi(**data.dict())
    return await create_satin_alma_talebi(db, db_item)