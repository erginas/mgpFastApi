from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.formul_degiskeni import FormulDegiskeni, FormulDegiskeniCreate
from models.formul_degiskeni import FormulDegiskeni as DBFormulDegiskeni
from crud.formul_degiskeni import get_all_formul_degiskeni, get_formul_degiskeni_by_id, create_formul_degiskeni

router = APIRouter(prefix='/formul_degiskeni', tags=['FormulDegiskeni'])

@router.get('/', response_model=list[FormulDegiskeni])
async def list_formul_degiskeni(db: AsyncSession = Depends()):
    return await get_all_formul_degiskeni(db)

@router.get('/{id}', response_model=FormulDegiskeni)
async def get_formul_degiskeni_item(id: int, db: AsyncSession = Depends()):
    result = await get_formul_degiskeni_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FormulDegiskeni)
async def create_formul_degiskeni_item(data: FormulDegiskeniCreate, db: AsyncSession = Depends()):
    db_item = DBFormulDegiskeni(**data.dict())
    return await create_formul_degiskeni(db, db_item)