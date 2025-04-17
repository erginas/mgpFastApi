from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sistem_rolu_formu import SistemRoluFormu, SistemRoluFormuCreate
from models.sistem_rolu_formu import SistemRoluFormu as DBSistemRoluFormu
from crud.sistem_rolu_formu import get_all_sistem_rolu_formu, get_sistem_rolu_formu_by_id, create_sistem_rolu_formu

router = APIRouter(prefix='/sistem_rolu_formu', tags=['SistemRoluFormu'])

@router.get('/', response_model=list[SistemRoluFormu])
async def list_sistem_rolu_formu(db: AsyncSession = Depends()):
    return await get_all_sistem_rolu_formu(db)

@router.get('/{id}', response_model=SistemRoluFormu)
async def get_sistem_rolu_formu_item(id: int, db: AsyncSession = Depends()):
    result = await get_sistem_rolu_formu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SistemRoluFormu)
async def create_sistem_rolu_formu_item(data: SistemRoluFormuCreate, db: AsyncSession = Depends()):
    db_item = DBSistemRoluFormu(**data.dict())
    return await create_sistem_rolu_formu(db, db_item)