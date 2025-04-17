from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sevkiyat_log import SevkiyatLog, SevkiyatLogCreate
from models.sevkiyat_log import SevkiyatLog as DBSevkiyatLog
from crud.sevkiyat_log import get_all_sevkiyat_log, get_sevkiyat_log_by_id, create_sevkiyat_log

router = APIRouter(prefix='/sevkiyat_log', tags=['SevkiyatLog'])

@router.get('/', response_model=list[SevkiyatLog])
async def list_sevkiyat_log(db: AsyncSession = Depends()):
    return await get_all_sevkiyat_log(db)

@router.get('/{id}', response_model=SevkiyatLog)
async def get_sevkiyat_log_item(id: int, db: AsyncSession = Depends()):
    result = await get_sevkiyat_log_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SevkiyatLog)
async def create_sevkiyat_log_item(data: SevkiyatLogCreate, db: AsyncSession = Depends()):
    db_item = DBSevkiyatLog(**data.dict())
    return await create_sevkiyat_log(db, db_item)