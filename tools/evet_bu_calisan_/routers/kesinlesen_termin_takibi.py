from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kesinlesen_termin_takibi import KesinlesenTerminTakibi, KesinlesenTerminTakibiCreate
from models.kesinlesen_termin_takibi import KesinlesenTerminTakibi as DBKesinlesenTerminTakibi
from crud.kesinlesen_termin_takibi import get_all_kesinlesen_termin_takibi, get_kesinlesen_termin_takibi_by_id, create_kesinlesen_termin_takibi

router = APIRouter(prefix='/kesinlesen_termin_takibi', tags=['KesinlesenTerminTakibi'])

@router.get('/', response_model=list[KesinlesenTerminTakibi])
async def list_kesinlesen_termin_takibi(db: AsyncSession = Depends()):
    return await get_all_kesinlesen_termin_takibi(db)

@router.get('/{id}', response_model=KesinlesenTerminTakibi)
async def get_kesinlesen_termin_takibi_item(id: int, db: AsyncSession = Depends()):
    result = await get_kesinlesen_termin_takibi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KesinlesenTerminTakibi)
async def create_kesinlesen_termin_takibi_item(data: KesinlesenTerminTakibiCreate, db: AsyncSession = Depends()):
    db_item = DBKesinlesenTerminTakibi(**data.dict())
    return await create_kesinlesen_termin_takibi(db, db_item)