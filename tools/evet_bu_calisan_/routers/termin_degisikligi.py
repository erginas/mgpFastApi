from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.termin_degisikligi import TerminDegisikligi, TerminDegisikligiCreate
from models.termin_degisikligi import TerminDegisikligi as DBTerminDegisikligi
from crud.termin_degisikligi import get_all_termin_degisikligi, get_termin_degisikligi_by_id, create_termin_degisikligi

router = APIRouter(prefix='/termin_degisikligi', tags=['TerminDegisikligi'])

@router.get('/', response_model=list[TerminDegisikligi])
async def list_termin_degisikligi(db: AsyncSession = Depends()):
    return await get_all_termin_degisikligi(db)

@router.get('/{id}', response_model=TerminDegisikligi)
async def get_termin_degisikligi_item(id: int, db: AsyncSession = Depends()):
    result = await get_termin_degisikligi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TerminDegisikligi)
async def create_termin_degisikligi_item(data: TerminDegisikligiCreate, db: AsyncSession = Depends()):
    db_item = DBTerminDegisikligi(**data.dict())
    return await create_termin_degisikligi(db, db_item)