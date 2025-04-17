from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.formul_degisken_degeri import FormulDegiskenDegeri, FormulDegiskenDegeriCreate
from models.formul_degisken_degeri import FormulDegiskenDegeri as DBFormulDegiskenDegeri
from crud.formul_degisken_degeri import get_all_formul_degisken_degeri, get_formul_degisken_degeri_by_id, create_formul_degisken_degeri

router = APIRouter(prefix='/formul_degisken_degeri', tags=['FormulDegiskenDegeri'])

@router.get('/', response_model=list[FormulDegiskenDegeri])
async def list_formul_degisken_degeri(db: AsyncSession = Depends()):
    return await get_all_formul_degisken_degeri(db)

@router.get('/{id}', response_model=FormulDegiskenDegeri)
async def get_formul_degisken_degeri_item(id: int, db: AsyncSession = Depends()):
    result = await get_formul_degisken_degeri_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FormulDegiskenDegeri)
async def create_formul_degisken_degeri_item(data: FormulDegiskenDegeriCreate, db: AsyncSession = Depends()):
    db_item = DBFormulDegiskenDegeri(**data.dict())
    return await create_formul_degisken_degeri(db, db_item)