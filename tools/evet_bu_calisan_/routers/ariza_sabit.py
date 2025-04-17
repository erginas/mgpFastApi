from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ariza_sabit import ArizaSabit, ArizaSabitCreate
from models.ariza_sabit import ArizaSabit as DBArizaSabit
from crud.ariza_sabit import get_all_ariza_sabit, get_ariza_sabit_by_id, create_ariza_sabit

router = APIRouter(prefix='/ariza_sabit', tags=['ArizaSabit'])

@router.get('/', response_model=list[ArizaSabit])
async def list_ariza_sabit(db: AsyncSession = Depends()):
    return await get_all_ariza_sabit(db)

@router.get('/{id}', response_model=ArizaSabit)
async def get_ariza_sabit_item(id: int, db: AsyncSession = Depends()):
    result = await get_ariza_sabit_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ArizaSabit)
async def create_ariza_sabit_item(data: ArizaSabitCreate, db: AsyncSession = Depends()):
    db_item = DBArizaSabit(**data.dict())
    return await create_ariza_sabit(db, db_item)